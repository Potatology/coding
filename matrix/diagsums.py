def diagonalSum(self, mat: List[List[int]]) -> int:
        diagSumright = 0
        diagSumleft = 0
        for i in range(len(mat)):
            diagSumleft += mat[i][i]
            diagSumright += mat[i][(len(mat)-1)-i]
        if len(mat[0]) % 2 != 0:
            diagSumright -= mat[len(mat)//2][len(mat)//2]
        return diagSumright + diagSumleft