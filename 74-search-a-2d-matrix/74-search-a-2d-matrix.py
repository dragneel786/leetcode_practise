class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        high = rows * cols - 1
        low = 0
        while(low <= high):
            mid = low + (high - low) // 2
            r = mid // cols
            c = mid % cols
            if(matrix[r][c] == target):
                return True
            
            if(matrix[r][c] < target):
                low = mid + 1
            else:
                high = mid - 1
        
        return False