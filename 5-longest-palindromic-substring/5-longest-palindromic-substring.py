class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        subStr = s[0]
        maxS = 1
        mat = [([0] * n) for _ in range(n)]
        for i in range(n):
            mat[i][i] = 1
            if(i < n - 1 and s[i] == s[i + 1]):
                mat[i][i + 1] = 2
                maxS = 2
                subStr = s[i : i + 2]


        for i in range(2, n):
            for j in range(i, n):
                if(s[j - i] == s[j] and mat[j - i + 1][j - 1]):
                    mat[j - i][j] = mat[j - i + 1][j - 1] + 2
                    if(maxS < mat[j - i][j]):
                        subStr = s[j - i: j + 1]
                        maxS = mat[j - i][j]
        return subStr