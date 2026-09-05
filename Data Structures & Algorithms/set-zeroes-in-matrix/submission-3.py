class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row = False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0

                    if i == 0:
                        first_row = True
                        continue
                    matrix[i][0] = 0
                    
        # Set rows to zeroes
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        # Set columns to zeroes
        for j in range(n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        if first_row:
            for j in range(n):
                matrix[0][j] = 0
        


        