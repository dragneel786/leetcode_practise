class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = ''.join(sorted(list(s1)))
        s2 = ''.join(sorted(list(s2)))
        idx1 = 0
        idx2 = 0
        print(s1, s2)
        while(s1[idx1] == s2[idx2]):
            idx1 += 1
            idx2 += 1
        
        if(s1[idx1] < s2[idx2]):
            s1, s2 = s2, s1
        
        while(idx1 < len(s1) and s1[idx1] >= s2[idx2]):
            idx1 += 1
            idx2 += 1
        
        return idx1 == len(s1)
        
        