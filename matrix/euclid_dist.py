"""
d(A, B) = sqrt(sum((A[i,j] — B[i,j])^2))
Где d(A, B) – евклидово расстояние между матрицами A и B
"""
import numpy as np
from icecream import ic

# np.random.seed(2) 

def calculate_euclide_dist(x1, x2):

    dists = np.zeros((len(x1[0]),len(x2[0])))
    for row in range(len(x1[0])):
        for column in range(len(x2[0])):
            # zeros_matrix[row][column] = (x1[row][column] - x2[row][column])**2
            diff = x1[column] - x2[row]
            # ic(diff)
            # dists[row, column] = np.sqrt(diff @ diff.T) # The @ operator can be used as a shorthand for np.matmul on ndarrays.
            dists[row, column] = np.sqrt(np.matmul(diff, diff.T))
    
    return dists


def distance_pairwise(x1, x2):
    ic(np.sum(x1**2, axis=1))
    ic(np.sum(x2**2, axis=1))
    P = np.add.outer(np.sum(x1**2, axis=1), np.sum(x2**2, axis=1))
    N = np.dot(x1, x2.T)
    return np.sqrt(P - 2 * N)



x1 = np.random.randint(5, size=(3, 2))
x2 = np.random.randint(5, size=(3, 2))
# x1 = np.array(([1,2], [2,1]))
# x2 = np.array(([3,4], [4,3]))
ic(x1, x2)
# ic(calculate_euclide_dist(x1, x2))
# ic(distance_pairwise(x1, x2))

ic(np.argsort(x1))