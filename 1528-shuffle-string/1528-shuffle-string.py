class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s = list(s)
        for i in range(len(s)):
            while(indices[i] != i):
                s[i], s[indices[i]] = s[indices[i]], s[i]
                idx = indices[i]
                indices[i], indices[idx] =\
                indices[idx], indices[i] 
        
        return ''.join(s)