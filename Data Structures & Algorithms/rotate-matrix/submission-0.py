class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(i+1,cols):
                topRightCell = matrix[i][j]
                bottomLeftCell = matrix[j][i]
                tmp=bottomLeftCell
                matrix[j][i] = topRightCell
                matrix[i][j] = tmp
        for i in range(rows):
            matrix[i] = matrix[i][::-1]
            


        