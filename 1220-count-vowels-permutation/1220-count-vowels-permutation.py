class Solution:
    def countVowelPermutation(self, n: int) -> int:
        M = (10 ** 9) + 7
        # a:0, e:1, i:2, o:3, u:4 
        paths = {0:[1], 1:[0, 2], 2:[0, 1, 3, 4], 3:[4, 2], 4:[0]}
    
        dp = [1] * 5
        for _ in range(n - 1):
            temp = [0] * 5
            for i in range(5):
                temp[i] = sum(dp[v] for v in paths[i]) % M
            dp = temp
        return sum(dp) % M
        
            