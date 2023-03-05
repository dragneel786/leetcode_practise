class Solution:
    def oddString(self, words: List[str]) -> str:
        
        def compute(w):
            ans = []
            for i in range(1, len(w)):
                ans.append(str(ord(w[i]) - ord(w[i - 1])))
            
            return '|'.join(ans)
        
        pattern = compute(words[0])
        c = 1
        for w in words[1:]:
            npattern = compute(w)
            if(pattern != npattern):
                if(c > 1):
                    return w
                else:
                    break
            
            c += 1
        return words[0] if(pattern != compute(words[-1])) else w
                
                