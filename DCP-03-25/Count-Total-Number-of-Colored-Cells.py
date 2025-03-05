class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1

        ans = 4
        res = 5
        for i in range(3, n + 1):
            res += (ans + 4)
            ans += 4
        
        return res
            

        
        return ans