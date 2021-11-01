import trigrid
import matplotlib.pyplot as plt
from math import cos, sin, pi
import numpy as np

def test_basic_grid():
    grid = trigrid.grid(2, 10)
    plt.plot(*grid, 'x')
    plt.show()


def test_rotated_grid():
    grid = trigrid.grid(2, 10, 30)
    plt.plot(*grid, 'x')
    plt.show()

def test_bounded_grid():
    bounds = [[15*cos(a), 15*sin(a)] for a in np.linspace(0, 2*pi, 100)]
    grid = trigrid.grid(1, 30, 0, bounding_shape=bounds)
    plt.plot(*grid, 'x')
    plt.show()

test_bounded_grid()