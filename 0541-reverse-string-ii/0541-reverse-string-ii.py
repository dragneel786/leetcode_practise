class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        def rivers(left, right):
            while(left < right):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            
        
        n = len(s)
        s = list(s)
        
        for i in range(0, n, 2 * k):
            rivers(i, min(i + k - 1, n - 1))
        
        return "".join(s)