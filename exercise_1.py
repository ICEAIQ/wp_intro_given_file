import numpy as np



def kroneckerProduct(left_matrix, right_matrix):
    pass

if __name__ == '__main__':
    m1 = [5]
    m2 = [7]
    result = kroneckerProduct(m1, m2)
    reference = [35]
    assert np.array_equal(result, reference)

    m1 = [[2]]
    m2 = [[4, 5],
          [6, 7]]
    result = kroneckerProduct(m1, m2)
    reference = [[8, 10],
                 [12, 14]]
    assert np.array_equal(result, reference)

    m1 = [[1, 2]]
    m2 = [[4, 5],
          [6, 7]]
    result = kroneckerProduct(m1, m2)
    reference = [[4, 5, 8, 10],
                 [6, 7, 12, 14]]
    assert np.array_equal(result, reference)
