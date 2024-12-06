class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        choosed = tot = 0
        for v in range(1, n + 1):
            if v in banned:
                continue
                
            if v + tot > maxSum:
                break

            tot += v
            choosed += 1
        
        return choosed
            