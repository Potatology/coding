def setZeroes():
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    H = [False]*len(matrix)
    W = [False]*len(matrix[0])
    
    for row in range(len(H)):
        for col in range(len(W)):
            if matrix[row][col] == 0:
                H[row] = True
                W[col] = True
    
    for row in range(len(H)):
        for col in range(len(W)):
            if H[row] == True or W[col] == True:
                matrix[row][col] = 0
    
    print(f'H {H} and W {W}')
    print(matrix)
    
    
                
        
setZeroes()
