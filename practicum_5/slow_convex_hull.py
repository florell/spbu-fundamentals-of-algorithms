import numpy as np
from numpy.typing import NDArray

from src.plotting import plot_points


def signed_area(p: NDArray, q: NDArray, r: NDArray) -> bool:

    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################

    pass


def slow_convex_hull(points: NDArray) -> NDArray:

    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################

    pass


if __name__ == "__main__":
    points = np.loadtxt("practicum_5/points_1.txt")
    plot_points(points, markersize=20)

    # Slow convex hull. Trivial to implement, but O(N^3)
    print("Slow convex hull")
    print("-" * 32)
    convex_hull = slow_convex_hull(points)
    plot_points(points, convex_hull=convex_hull, markersize=20)
    print()
