""" Write a function that takes in two integer matrices and multiplies them together.
Both matrices will be sparse, meaning that most of their elements will be zero. Take advantage of that to reduce the number of total computations that your function performs.
If the matrices cant be multiplied together, your function should return [ [] ] .
Sample input:
matrix_a = [
[0, 2, 0],
[0, -3, 5],
]
matrix_b = [
[0, 10, 0],
[0, 0, 0],
[0,	0,	4],
]


 """
def sparse_matrix_multiplication(matrix_a, matrix_b):
    # Write your code here.
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]
    # print(matrix_a)
    # list_a = make_list(matrix_a)
    # print(matrix_b)
    list_b = make_col_list(matrix_b)
    # print(list_b)
    matrix_c = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]
    # print(matrix_c)
    return fill_matric_c(matrix_c, matrix_a, list_b)


def fill_matric_c(matrix, list_a, list_b):
    for i in range(len(list_a)):

        # max_j = len(list_a[i])
        print(list_a[i])
        for k in range(len(list_b)):
            sum_row_col = 0
            for j in range(len(list_a[i])):
                #                print('list a ', list_a[i][j])
                #                print('list b ', list_b[k][j])
                if list_a[i][j] != 0 and list_b[k][j] != 0:
                    sum_row_col = sum_row_col + list_a[i][j] * list_b[k][j]
            matrix[i][k] = sum_row_col
            # print(sum_row_col)

    return matrix


def make_col_list(matrix):
    result_list = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    i = 0
    for row in result_list:
        j = 0
        for col in (row):
            result_list[i][j] = matrix[j][i]
            j += 1
        i += 1
    return result_list