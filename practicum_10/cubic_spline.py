import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt


def qubic_spline_coeff(x_nodes: NDArray, y_nodes: NDArray) -> NDArray:
    n = len(x_nodes)
    h = np.diff(x_nodes)
    y_diff = np.diff(y_nodes)
    alpha = np.zeros(n)
    for i in range(1, n - 1):
        alpha[i] = (3 / h[i]) * (y_diff[i] / h[i] - y_diff[i - 1] / h[i - 1])
    l = np.zeros(n)
    mu = np.zeros(n)
    z = np.zeros(n)
    l[0] = 1
    mu[0] = 0
    z[0] = 0
    for i in range(1, n - 1):
        l[i] = 2 * (x_nodes[i + 1] - x_nodes[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]
    l[n - 1] = 1
    z[n - 1] = 0
    c = np.zeros(n)
    b = np.zeros(n)
    d = np.zeros(n)
    for j in range(n - 2, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (y_diff[j] / h[j]) - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])
    coeff = np.zeros((n - 1, 4))
    for k in range(n - 1):
        coeff[k] = np.array([y_nodes[k], b[k], c[k], d[k]])
    return coeff


def qubic_spline(x: float, x_nodes: NDArray, qs_coeff: NDArray) -> float:
    n = len(x_nodes)
    for i in range(n - 1):
        if x_nodes[i] <= x <= x_nodes[i + 1]:
            h = x_nodes[i + 1] - x_nodes[i]
            t = (x - x_nodes[i]) / h
            a, b, c, d = qs_coeff[i]
            return a + b * t + c * t**2 + d * t**3


if __name__ == "__main__":
    # Let's build a cubic spline and use it to interpolate GRP

    gdp = np.array(
        [
            506500154001.466,
            516814258695.568,
            517962962962.963,
            460290556900.726,
            435083713850.837,
            395077301248.464,
            395531066563.296,
            391719993756.828,
            404926534140.017,
            270953116950.026,
            195905767668.562,
            259708496267.33,
            306602673980.117,
            345110438692.185,
            430347770731.787,
            591016690742.798,
            764017107992.391,
            989930542278.695,
            1299705247685.76,
            1660844408499.61,
            1222643696991.85,
            1524916112078.87,
            2031768558635.85,
            2170143623037.67,
            2230625004653.55,
            2063662281005.13,
            1365865245098.18,
            1283162348132.8,
        ]
    )
    years = np.arange(1989.0, 2017.0)
    x = np.linspace(years[0], years[-1], 500)
    coeffs = qubic_spline_coeff(years, gdp)
    spline_vectorized = np.vectorize(qubic_spline, excluded=set((1, 2)))
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    ax.plot(years, gdp, "x", markersize=10)
    ax.plot(x, spline_vectorized(x, years, coeffs))
    ax.grid()
    plt.show()
