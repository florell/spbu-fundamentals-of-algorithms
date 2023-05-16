from typing import Callable

import numpy
import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt


def lagrange_basis(i: int, x: float, x_nodes: NDArray):
    ch = 1
    zn = 1
    for j in range(len(x_nodes)):
        ch *= (x - x_nodes[j])
        if i != j:
            zn *= (x_nodes[i] - x_nodes[j])

    return ch / zn


def lagrange_interpolant(x: float, x_nodes: NDArray, y_nodes: NDArray):
    res = 0
    for i in range(len(y_nodes)):
        res += y_nodes[i] * lagrange_basis(i, x_nodes[i], x_nodes)


def plot_data_and_interpolant(x_nodes: NDArray, f: Callable[[float], float]):
    lnsp = np.linspace(x_nodes[0], x_nodes[-1], x_nodes.size * 10)
    oldf = f(lnsp)

    fig, ax = plt.subplots()
    ax.plot(lnsp, oldf)
    ax.grid(which="major", linewidth=1.2)
    ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5)
    ax.scatter(x_nodes, [f(i) for i in x_nodes], c="red")

    newf = list(map(lambda y: lagrange_interpolant(y, x_nodes, [f(i) for i in x_nodes]), lnsp))
    ax.plot(lnsp, newf)
    plt.show()




def runge_func(x: float) -> float:
    return 1.0 / (1 + 25 * x**2)


if __name__ == "__main__":
    # Let's implement optimal Lagrange interpolation and check it
    # on the Runge function

    # Equispaced nodes
    n = 11
    x_equi_nodes = np.linspace(-1.0, 1.0, n)
    plot_data_and_interpolant(x_equi_nodes, runge_func)

    # Optimally located nodes

    ##########################
    ### PUT YOUR CODE HERE ###
    ##########################

    x_opt_nodes = None  # should be filled
    plot_data_and_interpolant(x_opt_nodes, runge_func)
