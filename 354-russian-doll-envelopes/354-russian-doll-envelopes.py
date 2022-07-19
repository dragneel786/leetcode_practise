class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        def getIndex():
            low, high = 0, len(dp) - 1
            res = -1
            while(low <= high):
                mid = ((high - low) >> 1) + low
                if(dp[mid][0] < envelopes[i][0] and\
                  dp[mid][1] < envelopes[i][1]):
                    low = mid + 1
                    res = mid
                else:
                    high = mid - 1
            return res + 1
        
        envelopes.sort(key=lambda x:[x[0], -x[1]])
        n = len(envelopes)
        dp = [[inf,inf] for _ in range(n)]
        dp[0] = envelopes[0]
        counts = 1
        for i in range(1, n):
            idx = getIndex()
            counts = max(idx + 1, counts)
            dp[idx] = envelopes[i]
        return counts
            