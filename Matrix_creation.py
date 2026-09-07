# Create an identity matrix of the specified size ( >= 0 ).

# Some examples:

# (1)  =>  [[1]]

# (2) => [ [1,0],
#          [0,1] ]

#        [ [1,0,0,0,0],
#          [0,1,0,0,0],
# (5) =>   [0,0,1,0,0],
#          [0,0,0,1,0],
#          [0,0,0,0,1] ]   

def get_matrix(n):
    if n == 0:
        return []
    
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        matrix[i][i] = 1
    
    return matrix