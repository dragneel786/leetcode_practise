class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [([0] * n) for _ in range(n)]
        up = left = 0
        down = right = n
        val = 1
        while(up < down and left < right):
            for u in range(left, right):
                ans[up][u] = val
                val += 1
            up += 1
            
            for r in range(up, down):
                ans[r][right - 1] = val
                val += 1
            right -= 1
            
            if(up < down):
                for d in range(right - 1, left - 1, -1):
                    ans[down - 1][d] = val
                    val += 1
                down -= 1
            
            if(left < right):
                for l in range(down - 1, up - 1, -1):
                    ans[l][left] = val
                    val += 1
                left += 1
            
        return ans
            
            