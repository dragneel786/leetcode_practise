class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if(n == k):
            return sum(cardPoints)
        
        w = n - k
        res = math.inf
        j = curr = 0
        tot = 0
        for i, c in enumerate(cardPoints):
            tot += c
            curr += c
            if(i - j + 1 > w):
                curr -= cardPoints[j]
                j += 1
            
            if(i - j + 1 == w):
                res = min(res, curr)
            
        return tot - res
                
        