class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for i in range(min(n, limit) + 1):
            if n - i <= 2 * limit:
                res += min(limit, n - i) - max(0, n - i - limit) + 1
            
        return res