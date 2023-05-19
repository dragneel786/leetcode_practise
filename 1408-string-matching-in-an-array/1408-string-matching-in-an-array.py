class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        words.sort(key=lambda x: len(x))
        for i, w1 in enumerate(words):
            for w2 in words[i + 1:]:
                if(w1 in w2):
                    ans.append(w1)
                    break
                    
        return ans