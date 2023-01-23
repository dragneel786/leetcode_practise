class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ss = [''] * len(s)
        for i in range(len(s)):
            ss[indices[i]] = s[i]
        
        return ''.join(ss)