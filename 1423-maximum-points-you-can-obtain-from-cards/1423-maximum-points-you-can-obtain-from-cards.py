class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        ksums = 0
        for i in range(k):
            ksums += cardPoints[i]
            
        if(n == k):
            return ksums
        
        maxSum = ksums
        n, k = n - 1, k - 1
        while(k > -1):
            add, sub = cardPoints[n], cardPoints[k]
            ksums = ksums - sub + add
            maxSum = max(maxSum, ksums)
            n, k = n - 1, k - 1
        
        return maxSum
        
        