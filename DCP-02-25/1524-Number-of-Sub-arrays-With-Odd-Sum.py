class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j: continue
                if word1 in word2:
                    res.append(word1)
                    break
        
        return res