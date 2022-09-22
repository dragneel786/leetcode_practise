class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def char_counts(s):
            s += " "
            count = 1
            ret = []
            for i in range(1, len(s)):
                if(s[i - 1] != s[i]):
                    ret.append([s[i - 1], count])
                    count = 0
                
                count += 1
            
            return ret
        
        count = 0
        scount = char_counts(s)
        for word in words:
            wcount = char_counts(word)
            if(len(scount) != len(wcount)):
                continue
            
            for a, b in zip(scount, wcount):
                if(a[0] == b[0] and \
                   (a[1] == b[1] or\
                   a[1] > b[1] and a[1] > 2)):
                    continue
                break
            else:
                count += 1
        
        return count
            
                    
                    
                
        
        
        