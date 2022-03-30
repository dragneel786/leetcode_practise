class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        h = m - 1
        row = -1
        while(l <= h):
            mid = l + (h - l) // 2
            if(row != -1 and matrix[row][mid] == target):
                return True
            
            elif(row == -1 and matrix[mid][0] <= target and matrix[mid][n - 1] >= target):
                row = mid
                l = 0
                h = n - 1
                
            elif((row  == -1 and matrix[mid][0] > target) or (row != -1 and matrix[row][mid] > target)):
                h = mid - 1
                
            else:
                l = mid + 1
        
        return False
        
                