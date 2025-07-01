class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        curr, count = "", 1
        for c in word:
            if c != curr:
                res += (count - 1)
                count = 0
            
            curr = c
            count += 1   

        return res + count - 1





                

        
        