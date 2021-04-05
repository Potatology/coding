matrix =    [[7,3,1,9],
            [3,4,6,9],
            [6,9,6,6],
            [9,5,8,5]]

diagSumright = 0
diagSumleft = 0
for i in range(len(matrix)):
    diagSumleft += matrix[i][i]
    diagSumright += matrix[i][(len(matrix)-1)-i]
# for i in range(len(matrix)):
    # diagSumright += matrix[i][(len(matrix)-1)-i]
if len(matrix[0]) % 2 != 0:
    diagSumright -= matrix[len(matrix)//2][len(matrix)//2]


print(f'left: {diagSumleft}, right: {diagSumright}')        
