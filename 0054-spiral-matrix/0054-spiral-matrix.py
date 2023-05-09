class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        rows, cols = len(matrix), len(matrix[0])
        
        up, right = 0, cols
        down, left = rows, 0
        
        while(up < down and left < right):
            
            for u in range(left, right):
                ans.append(matrix[up][u])
            up += 1
            
            for r in range(up, down):
                ans.append(matrix[r][right - 1])
            right -= 1
            
            if(up < down):
                for d in range(right - 1, left - 1, -1):
                    ans.append(matrix[down - 1][d])
            down -= 1
            
            if(left < right):
                for l in range(down - 1, up - 1, -1):
                    ans.append(matrix[l][left])
            left += 1
            
        return ans
    
            
            