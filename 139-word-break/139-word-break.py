class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        isBreakable = False
        idx = [n]
        for i in range(n - 1, -1, -1):
            isBreakable = False
            for j in idx:
                if(s[i: j] in wordDict):
                    isBreakable = True
                    idx = [i] + idx
                    break

        return isBreakable