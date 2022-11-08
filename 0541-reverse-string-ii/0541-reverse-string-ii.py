class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        s = list(s)
        
        for i in range(0, n, 2 * k):
            left, right = i, min(i + k, n)
            s[left: right] = s[left: right][::-1]
        
        return "".join(s)