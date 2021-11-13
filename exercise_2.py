import numpy as np


def computeMatrix(baseMatrix, nbQbit, fQbit):
    pass

if __name__ == '__main__':
    m = [[5]]
    arr = [[5]]
    assert (np.array_equal(computeMatrix(m, 1, 0), arr))
    m = [[5]]
    arr = [[5.0, 0], [0, 5.0]]
    assert (np.array_equal(computeMatrix(m, 2, 0), arr))
    m = [[0, 1], [1, 0]]
    arr = [[0., 1., 0., 0.], [1., 0., 0., 0.], [0., 0., 0., 1.], [0., 0., 1., 0.]]
    assert (np.array_equal(computeMatrix(m, 2, 0), arr))
    m = [[1, 2], [3, 4]]
    arr = [[1., 0., 2., 0.], [0., 1., 0., 2.], [3., 0., 4., 0.], [0., 3., 0., 4.]]
    assert (np.array_equal(computeMatrix(m, 2, 1), arr))
    m = [[1, 2], [3, 4]]
    arr = np.kron(np.kron(np.identity(2), m), np.identity(2))
    assert (np.array_equal(computeMatrix(m, 3, 1), arr))