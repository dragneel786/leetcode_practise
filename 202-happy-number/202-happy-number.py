class Solution:
    def isHappy(self, n: int) -> bool:
        lookup = set()
        while(n not in lookup):
            lookup.add(n)
            temp = n
            n = 0
            while(temp != 0):
                rem = temp % 10
                temp //= 10
                n += (rem ** 2)
            
            if(n == 1):
                return True
            
        return False