class Solution:
    def isHappy(self, n: int) -> bool:
        fast, slow = n, n
        while(True):
            slow = self.getSquareSum(slow)
            fast = self.getSquareSum(self.getSquareSum(fast))
            if(slow == fast):
                break

        if(slow == 1):
            return True
        return False

    def getSquareSum(self, n):
        temp = n
        n = 0
        while(temp):
            rem = (temp % 10)
            temp //= 10
            n += (rem ** 2)
        return n
#         lookup = set()
#         while(n not in lookup):
#             lookup.add(n)
#             temp = n
#             n = 0
#             while(temp != 0):
#                 rem = temp % 10
#                 temp //= 10
#                 n += (rem ** 2)
            
#             if(n == 1):
#                 return True
            
#         return False