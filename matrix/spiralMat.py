def spiralOrder():
    matrix = [[0, 4, 8, 12], 
            [1, 5, 9, 13], 
            [2, 6, 10, 14], 
            [3, 7, 11, 15]]
    res = []
    height = len(matrix)
    
    for i in range(height):
        res.append([0]*height)
    
    for i in range(height):
        for j in range(height):
            res[j][height - i -1] = matrix[i][j]
    return res

def printSpiral():
    res = []
    height = len(matrix)
    
    for i in range(height):
        for j in range(height):
            res.append(matrix[height - 1 - j][i])
    return res

def transpose():
    matrix = [[0,1,2], 
                [3,4,5], 
                [6,7,8]]
    
    height = len(matrix)
    
    for i in range(height):
        for j in range(i, height):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    return matrix

print(transpose())