class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m - 1
        while(low <= high):
            mid = low + ((high - low) // 2)
            if(matrix[mid][0] <= target <= matrix[mid][-1]):
                idx = bisect_left(matrix[mid], target)
                return matrix[mid][idx] == target
            
            if(matrix[mid][0] > target):
                high = mid - 1
            else:
                low = mid + 1
        
        return False
            
            
        
        
        