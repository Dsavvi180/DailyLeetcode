class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        for i in zero_rows:
            for j in range(COLS):
                matrix[i][j] = 0
        
        for i in range(ROWS):
           for j in zero_cols:
               matrix[i][j] = 0

        

            

        
        