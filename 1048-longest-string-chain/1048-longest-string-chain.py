class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        if(n == 1):
            return 1
        
        def isSubseq(w1, w2):
            j = 0
            n = len(w2)
            for i in range(len(w1)):
                if(j == n):
                    break
                
                if(w1[i] == w2[j]):
                    j += 1
                    
            if(j == n):
                return True
            return False
            
        words.sort(key=lambda s: len(s))
        dp = [0] * n
        dp[0] = 1
        res = 1
        for i in range(1, n):
            maxChain = 0
            for j in range(i - 1, -1, -1):
                diff = len(words[i]) - len(words[j])
                if(diff > 1):
                    break
                
                if(diff and isSubseq(words[i], words[j])):
                    maxChain = max(maxChain, dp[j])
                
            dp[i] = maxChain + 1
            res = max(dp[i], res)
        return res
        