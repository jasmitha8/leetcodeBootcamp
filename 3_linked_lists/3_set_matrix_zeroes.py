class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        rowSet, colSet = set(), set()
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)
                    
        for k in range(rows):
            for l in range(cols):
                if k in rowSet or l in colSet:
                    matrix[k][l]=0
