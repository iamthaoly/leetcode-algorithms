class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Solution 2
        n = len(matrix)
        matrix.reverse()
        for i in range(0, n):
            for j in range(i + 1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
