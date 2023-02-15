class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        carry = 0
        ans = deque()
        for a, b in zip_longest(num[::-1], str(k)[::-1], fillvalue = 0):
            carry += a + int(b)            
            ans.appendleft(carry % 10)
            carry //= 10
        
        if(carry):
            ans.appendleft(carry)
        
        return ans
            