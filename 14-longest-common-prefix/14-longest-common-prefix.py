class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = float('inf')
        for i in strs:
            minLen = min(minLen, len(i))

        if(minLen == 0):
            return ""

        res = ""
        for i in range(minLen):
            res += strs[0][i]
            for str in strs:
                if(res[-1] != str[i]):
                    return res[0: len(res) - 1]

        return res