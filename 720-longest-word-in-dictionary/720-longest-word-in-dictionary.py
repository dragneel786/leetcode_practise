class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = set(words)
        ans = ""
        for w in words:
            if(len(ans) <= len(w)):
                present = True
                for i in range(len(w) - 1, 0, -1):
                    if(w[0: i] not in words):
                        present = False
                        break
                if(present):
                    if(len(ans) < len(w)):
                        ans = w
                    else:
                        ans = min(ans, w)
        return ans
                    

                
        
                
        
        