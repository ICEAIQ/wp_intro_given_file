from exercise_1 import kroneckerProduct
from exercise_3 import XOR


import numpy as np
def evaluate_kronecker_product_1():
    m1 = [51]
    m2 = [71]
    result = kroneckerProduct(m1, m2)
    reference = [51*71]
    is_equal = np.array_equal(result, reference)
    return is_equal

def evaluating_kronecker_product_2():
    m1 = [[4, 5],[6, 7]]
    m2 = [[1, 2]]
    result = kroneckerProduct(m1, m2)
    reference = [[4, 8, 5, 10],[6, 12, 7, 14]]
    return np.array_equal(result, reference)

def evaluating_XOR():
    array = [XOR(0, 0) == 0,XOR(0, 1) == 1,XOR(1, 0) == 1,XOR(1, 1) == 0]
    boolean = True
    for i in array:
        boolean = boolean and i
    return boolean

def execute_one_evaluation(evaluating_lambda):
    boolean = False
    try:
        boolean = evaluating_lambda()
    except:
        pass
    return boolean

def testComputeMatrix():
    from exercise_2 import computeMatrix
    m = [[0,1],[1,0]]
    arr = [[0., 1., 0., 0.], [1., 0., 0., 0.],[0., 0., 0., 1.],[0., 0., 1., 0.]]
    t3_1 = np.array_equal(computeMatrix(m,2,0), arr)
    m = [[0,1],[1,0]]
    arr = [[0., 0., 1., 0.],[0., 0., 0., 1.],[1., 0., 0., 0.],[0., 1., 0., 0.]]
    t3_2 = np.array_equal(computeMatrix(m,2,1), arr)
    return t3_1 and t3_2

def evaluating_script():
    t2 = execute_one_evaluation(evaluate_kronecker_product_1)
    t3 = execute_one_evaluation(evaluating_kronecker_product_2)
    t4 = execute_one_evaluation(evaluating_XOR)
    t5 = execute_one_evaluation(testComputeMatrix)
    mark = 0
    if t2:
        mark += 3
    if t3:
        mark += 2
    if t4:
        mark += 5
    print(t4)
    if t5:
        mark += 10

    print("Your mark is: ",mark)
    return mark

if __name__ == '__main__':
    print(evaluating_XOR())
    evaluating_script()