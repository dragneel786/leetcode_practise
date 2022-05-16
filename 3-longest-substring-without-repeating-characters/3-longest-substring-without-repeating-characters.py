class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashed = defaultdict(lambda:-1)
        n = len(s)
        i = 0
        j = 0
        maxL = 0
        while(j < n):
            if(hashed[s[j]] != -1):
                print(hashed[s[j]], j)
                maxL = max(maxL, j - i)
                i = max(i, hashed[s[j]] + 1)
            hashed[s[j]] = j
            j += 1
        maxL = max(maxL, j - i)
        return maxL
            