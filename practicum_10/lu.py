import numpy as np
from numpy.typing import NDArray


def lu(A: NDArray, permute: bool) -> tuple[NDArray, NDArray, NDArray]:
    n = A.shape[0]  # Get the size of the matrix A

    L = np.eye(n)  # Create an identity matrix L of size n
    U = np.copy(A)  # Create a copy of the input matrix A
    P = np.eye(n)  # Create an identity matrix P of size n

    for k in range(n - 1):
        if permute:
            pivot = np.argmax(abs(U[k:, k])) + k  # Find the index of the row with the maximum absolute value in column k
            U[[k, pivot]] = U[[pivot, k]]  # Swap rows in matrix U
            P[[k, pivot]] = P[[pivot, k]]  # Swap rows in matrix P
            if k:
                L[[k, pivot], :k] = L[[pivot, k], :k]  # Swap rows in matrix L up to column k

        if abs(U[k, k]) < 1e-12:
            raise ValueError("Pivoting failed. The matrix is singular or ill-conditioned.")

        for j in range(k + 1, n):
            L[j, k] = U[j, k] / U[k, k]  # Compute the elements of matrix L
            U[j, k:] -= L[j, k] * U[k, k:]  # Compute the elements of matrix U

    return L, U, P


def solve(L: NDArray, U: NDArray, P: NDArray, b: NDArray) -> NDArray:
    n = L.shape[0]
    y = np.zeros(n)  # Create a vector y of size n filled with zeros
    x = np.zeros(n)  # Create a vector x of size n filled with zeros
    b = np.dot(P, b)  # Multiply the permutation matrix P with the vector b

    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])  # Compute the elements of vector y

    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]  # Compute the elements of vector x

    return x


def get_A_b(a_11: float, b_1: float) -> tuple[NDArray, NDArray]:
    A = np.array([[a_11, 1.0, -3.0], [6.0, 2.0, 5.0], [1.0, 4.0, -3.0]])  # Create matrix A
    b = np.array([b_1, 12.0, -39.0])  # Create vector b
    return A, b


if __name__ == "__main__":
    p = 9  # Modify from 7 to 16 to check instability
    a_11 = 3 + 10 ** (-p)  # Add/remove 10**(-p) to check instability
    b_1 = -16 + 10 ** (-p)  # Add/remove 10**(-p) to check instability
    A, b = get_A_b(a_11, b_1)

    # With pivoting
    L, U, P = lu(A, permute=True)
    x = solve(L, U, P, b)
    assert np.all(np.isclose(x, [1, -7, 4])), f"The anwser {x} is not accurate enough"
    # Without pivoting
    L, U, P = lu(A, permute=False)
    x_ = solve(L, U, P, b)
    assert np.all(np.isclose(x_, [1, -7, 4])), f"The anwser {x_} is not accurate enough"
