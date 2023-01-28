class Solution:
    def largestInteger(self, num: int) -> int:
        evens = []
        odds = []
        num = list(map(int, str(num)))
        for n in num:
            if(n & 1):
                odds.append(n)
            else:
                evens.append(n)
        
        evens.sort()
        odds.sort()
        ans = 0
        for n in num:
            ans *= 10
            if(n & 1):
                ans += odds.pop()
            else:
                ans += evens.pop()
        
        return ans