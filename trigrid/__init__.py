import numpy as np
from math import sqrt, sin, cos, radians
import matplotlib.path as mpath

__all__ = ['grid']


def grid(L, N, degrees=None, bounding_shape=None):
    """
    Creates a triangular grid

    :param L: spacing between lattice sites
    :param N:
    :param degrees: rotation angle of grid
    :return:
    """
    x = np.linspace(-N*L*sqrt(3)/2, N*L*sqrt(3)/2, 2*N+1)
    y = np.linspace(-N*L, N*L, 2*N+1)
    x, y = np.meshgrid(x, y)
    y[:, 1::2] += L/2
    points = np.array((x.ravel(), y.ravel()))

    if degrees is not None:
        points = rotate_grid(points, degrees)

    if bounding_shape is not None:
        path = mpath.Path(bounding_shape)
        inside = path.contains_points(points.T)
        points = points[:, inside]

    return points


def rotate_grid(points, deg):
    rads = radians(deg)
    M = np.array(((cos(rads), -sin(rads)), (sin(rads), cos(rads))))
    return M @ points