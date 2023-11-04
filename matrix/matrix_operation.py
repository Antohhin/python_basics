from icecream import ic

def matrix_sum():
    
    X = [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]

    Y = [[5,8,1],
        [6,7,3],
        [4,5,9]]

    result = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    for row_id in range(len(X)):
        for column_id in range(len(X[0])):
            result[row_id][column_id] = X[row_id][column_id] + Y[row_id][column_id]
            # ic(result)
    return result


ic(matrix_sum())

def matrix_multiplication():
    X = [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]

    Y = [[5,8,1],
        [6,7,3],
        [4,5,9]]

    result = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    for row_id in range(len(X)):
        for column_id in range(len(X[0])):
            result[row_id][column_id] = X[row_id][column_id] * Y[row_id][column_id]
            # ic(result)
    return result