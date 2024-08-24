class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        res = onesCount = zerosCount = 0
        onesIndex = zerosIndex = 0
        for i, c in enumerate(s):
            onesCount += c == '1'
            zerosCount += c == '0'
            
            while(onesCount > k and onesIndex < i):
                onesCount -= s[onesIndex] == '1'
                onesIndex += 1
            
            while(zerosCount > k and zerosIndex < i):
                zerosCount -= s[zerosIndex] == '0'
                zerosIndex += 1
            
            res += (i - min(onesIndex, zerosIndex) + 1)
        
        return res
        