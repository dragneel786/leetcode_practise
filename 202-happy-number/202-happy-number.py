class Solution:
    def isHappy(self, n: int) -> bool:
        lookup = set()
        while(n not in lookup):
            lookup.add(n)
            temp = 0
            while(n):
                rem = n % 10
                n //= 10
                temp += (rem ** 2)
            
            if(temp == 1):
                return True
            
            n = temp
            
        return False