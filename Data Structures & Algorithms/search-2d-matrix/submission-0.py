class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def find_row():
            low, high = 0, len(matrix) - 1
            while low <= high:
                mid = (low + high) // 2
                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    return mid
                elif target > matrix[mid][-1]:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        
        def find_col(row):
            low, high = 0, len(matrix[row])
            while low <= high:
                mid = (low + high) // 2
                if matrix[row][mid] == target:
                    return mid
                elif matrix[row][mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1


        r = find_row()
        if r == -1:
            return False

        return find_col(r) >= 0
        
        # low_i, high_i = 0, len(matrix) - 1
        # low_j, high_j = 0, len(matrix[0]) - 1

        # while low_i <= high_i and low_j <= high_j:
        #     mid_i, mid_j = (low_i + high_i) // 2, (low_j + high_j) // 2
        #     if matrix[mid_i][mid_j] == target:
        #         return True
        #     elif matrix[mid_i][mid_j] < target:
        #         low_i = mid_i + 1
        #         low_j = mid_j + 1
        #     else:
        #         high_i = mid_i - 1
        #         high_j = mid_j - 1
        # return False