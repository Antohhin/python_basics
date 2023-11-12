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


# ic(matrix_sum())

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
    
    # ic(len(X))
    # ic(len(X[0]))
    # row_num = len(X)
    # column_num = len(X[0])
    for row_id in range(len(X)):
        for column_id in range(len(X[0])):
            for Yrow_id in range(len(Y)):
                result[row_id][column_id] = result[row_id][column_id] + X[row_id][Yrow_id] * Y[Yrow_id][column_id]
                # result[row_id][column_id] += X[row_id][Yrow_id] * Y[Yrow_id][column_id]
                # dot_product = X[row_id][column_id] * Y[column_id][row_id]
                # dot_product2 = dot_product
            # ic(result)
    return result

# ic(matrix_multiplication())

def matrix_transponse():

    X = [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]

    Y = [[5,8,1],
        [6,7,3],
        [4,5,9]]

    result = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    
    # for row_id in range(len(X)):
        # for column_id in range(len(X[0])):
            # result[row_id][column_id] = X[column_id][row_id]

    result = [[X[j][i] for j in range(len(X[0]))] for i in range(len(X))] # через list comprehension
    return result

ic(matrix_transponse())