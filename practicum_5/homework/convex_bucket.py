from time import perf_counter

import numpy as np
from numpy.typing import NDArray
from src.plotting import plot_bucket


def convex_bucket(points: NDArray) -> NDArray:
    """Constructs the lower part of the convex hull"""
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    points = sorted(points, key=lambda p: (p[0], p[1]))

    lower = [points[0]]
    for i in range(1, len(points)):
        while len(lower) >= 2 and cross(lower[-2], lower[-1], points[i]) <= 0:
            lower.pop()
        # if len(lower) == 1 and points[i][0] == lower[0][0]:
        #     continue
        lower.append(points[i])


    return np.array(lower)


if __name__ == "__main__":
    for i in range(1, 11):
        txtpath = f"practicum_5/homework/points_{i}.txt"
        points = np.loadtxt(txtpath)
        print(f"Processing {txtpath}")
        print("-" * 32)
        t_start = perf_counter()
        ch = convex_bucket(points)
        t_end = perf_counter()
        print(f"Elapsed time: {t_end - t_start} sec")
        plot_bucket(points, convex_hull=ch, markersize=20)
        print()
