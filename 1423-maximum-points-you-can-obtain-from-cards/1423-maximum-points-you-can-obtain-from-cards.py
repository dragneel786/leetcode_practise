class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if(n == k):
            return sum(cardPoints)
        
        for i in range(1, n):
            cardPoints[i] += cardPoints[i - 1]
        
        res = cardPoints[-1]
        for i in range(k + 1):
            # print(cardPoints[i + (n - k) - 1])
            temp = cardPoints[i + (n - k) - 1]
            if(i > 0):
                temp -= cardPoints[i - 1]
            res = min(res, temp)
        
        return cardPoints[-1] - res
                
        