# Your task, is to create N×N multiplication table, of size provided in parameter.
#
# For example, when given size is 3:
#
# 1 2 3
# 2 4 6
# 3 6 9
# For the given example, the return value should be:
#
# [[1,2,3],[2,4,6],[3,6,9]]

def multiplication_table(size):
    if size == 1:
        return [[1]]
    matrix = [[i for i in range(1, size + 1)]]
    for i in matrix[0][1:]:
        result_matrix = []
        for j in range(1, size + 1):
            result_matrix.append(i * j)
        matrix.append(result_matrix)
    return matrix