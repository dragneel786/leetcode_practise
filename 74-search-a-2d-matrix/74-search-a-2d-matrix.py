class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        l = 0
        h = len(matrix) * n - 1
        while(l <= h):
            mid = l + (h - l) // 2
            val = matrix[mid // n][mid % n]
            if(val == target):
                return True
            elif(val > target):
                h = mid - 1
            else:
                l = mid + 1
        return False