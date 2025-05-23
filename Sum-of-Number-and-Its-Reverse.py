class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if not num:
            return True

        for val in range(num):
            temp = val
            rev = 0
            while(temp):
                rev = (rev * 10) + (temp % 10)
                temp //= 10
            
            if rev + val == num:
                return True
        
        return False