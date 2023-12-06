class Solution:
    def totalMoney(self, n: int) -> int:
        start = 0
        ans = 0
        while(n > 0):
            first = (start * (start + 1)) // 2
            if(n >= 7):
                adder = 7
            else:
                adder = n
            second = ((start + adder) * (start + adder + 1)) // 2
            ans += (second - first)
            start += 1
            n -= 7
        
        return ans