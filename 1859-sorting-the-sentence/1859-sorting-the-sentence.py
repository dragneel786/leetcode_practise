class Solution:
    def sortSentence(self, s: str) -> str:
        splits = s.split(" ")
        ans = [""] * len(splits)
        for w in splits:
            w, i = w[:-1], int(w[-1])
            ans[i - 1] = w
        
        return ' '.join(ans)
            
        