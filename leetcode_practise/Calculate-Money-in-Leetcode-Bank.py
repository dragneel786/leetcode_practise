class Solution:
    def totalMoney(self, n: int) -> int:
        start = 0
        res = 0
        while(start < n):
            curr = (start // 7) + 1
            for _ in range(start, min(start + 7, n)):
                res += curr
                curr += 1
                start += 1
                
        return res


