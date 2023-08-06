import os
from pathlib import PurePosixPath
from typing import Callable, MutableMapping, Optional

import numpy as np
import s3fs
import zarr
from affine import Affine


def get_env(key: str, default: Optional[str] = None) -> str:
    value = os.environ.get(key)
    if value is None:
        if default is not None:
            return default
        raise ValueError(f"environment variable {key} not present")
    else:
        return value


class ZarrReader:
    """Reads hazard event data from Zarr files, including OSC-format-specific attributes."""

    # environment variable names:
    __access_key = "OSC_S3_ACCESS_KEY"
    __secret_key = "OSC_S3_SECRET_KEY"
    __S3_bucket = "OSC_S3_BUCKET"  # e.g. redhat-osc-physical-landing-647521352890 on staging
    __zarr_path = "OSC_S3_HAZARD_PATH"  # e.g. hazard/hazard.zarr on staging

    def __init__(
        self,
        store: Optional[MutableMapping] = None,
        path_provider: Optional[Callable[..., str]] = None,
        get_env: Callable[[str, Optional[str]], str] = get_env,
    ):
        """Create a ZarrReader.

        Args:
            store: if not supplied, create S3Map store.
            path_provider: function that provides path to the data set based on a set ID.
            get_env: allows override obtaining of environment variables.
        """
        if store is None:
            # if no store is provided, attempt to connect to an S3 bucket
            if get_env is None:
                raise TypeError("if no store specified, get_env is required to provide credentials")

            access_key = get_env(self.__access_key, None)
            secret_key = get_env(self.__secret_key, None)
            s3_bucket = get_env(self.__S3_bucket, "redhat-osc-physical-landing-647521352890")
            zarr_path = get_env(self.__zarr_path, "hazard/hazard.zarr")

            s3 = s3fs.S3FileSystem(anon=False, key=access_key, secret=secret_key)

            store = s3fs.S3Map(
                root=str(PurePosixPath(s3_bucket, zarr_path)),
                s3=s3,
                check=False,
            )

        self._root = zarr.open(store, mode="r")
        self._path_provider = path_provider
        pass

    def get_curves(self, set_id, longitudes, latitudes, interpolation="floor"):
        """Get intensity curve for each latitude and longitude coordinate pair.

        Args:
            set_id: string or tuple representing data set, converted into path by path_provider.
            longitudes: list of longitudes.
            latitudes: list of latitudes.
            interpolation: interpolation method, "floor" or "linear".

        Returns:
            curves: numpy array of intensity (no. coordinate pairs, no. return periods).
            return_periods: return periods in years.
        """

        # assume that calls to this are large, not chatty
        if len(longitudes) != len(latitudes):
            raise ValueError("length of longitudes and latitudes not equal")
        path = self._path_provider(set_id) if self._path_provider is not None else set_id
        z = self._root[path]  # e.g. inundation/wri/v2/<filename>

        # OSC-specific attributes contain tranform and return periods
        t = z.attrs["transform_mat3x3"]  # type: ignore
        transform = Affine(t[0], t[1], t[2], t[3], t[4], t[5])
        return_periods = z.attrs["index_values"]  # type: ignore

        image_coords = self._get_coordinates(longitudes, latitudes, transform)

        res = z.shape
        print(res)

        if interpolation == "floor":
            image_coords = np.floor(image_coords).astype(int)
            iz = np.tile(np.arange(z.shape[0]), image_coords.shape[1])  # type: ignore
            iy = np.repeat(image_coords[1, :], len(return_periods))
            ix = np.repeat(image_coords[0, :], len(return_periods))

            data = z.get_coordinate_selection((iz, iy, ix))  # type: ignore
            return data.reshape([len(longitudes), len(return_periods)]), np.array(return_periods)

        elif interpolation == "linear":
            res = ZarrReader._linear_interp_frac_coordinates(z, image_coords, return_periods)
            return res, return_periods

        else:
            raise ValueError("interpolation must have value 'floor' or 'linear'")

    @staticmethod
    def _linear_interp_frac_coordinates(z, image_coords, return_periods):
        """Return linear interpolated data from fractional row and column coordinates."""
        icx = np.floor(image_coords[0, :]).astype(int)[..., None]
        xf = image_coords[0, :][..., None] - icx  # type: ignore
        # note periodic boundary condition
        ix = np.concatenate([icx, icx, (icx + 1) % z.shape[2], (icx + 1) % z.shape[2]], axis=1)[..., None].repeat(
            len(return_periods), axis=2
        )  # points, 4, return_periods

        icy = np.floor(image_coords[1, :]).astype(int)[..., None]
        yf = image_coords[1, :][..., None] - icy  # type: ignore
        iy = np.concatenate([icy, icy + 1, icy, icy + 1], axis=1)[..., None].repeat(len(return_periods), axis=2)

        iz = (
            np.arange(len(return_periods), dtype=int)[None, ...]
            .repeat(4, axis=0)[None, ...]
            .repeat(image_coords.shape[1], axis=0)
        )

        data = z.get_coordinate_selection((iz, iy, ix))  # type: ignore # index, row, column
        w0 = (1 - yf) * (1 - xf)
        w1 = yf * (1 - xf)
        w2 = (1 - yf) * xf
        w3 = yf * xf

        return data[:, 0, :] * w0 + data[:, 1, :] * w1 + data[:, 2, :] * w2 + data[:, 3, :] * w3

    @staticmethod
    def _get_coordinates(longitudes, latitudes, transform: Affine):
        coords = np.vstack((longitudes, latitudes, np.ones(len(longitudes))))  # type: ignore
        inv_trans = ~transform
        mat = np.array(inv_trans).reshape(3, 3)
        frac_image_coords = mat @ coords
        return frac_image_coords
