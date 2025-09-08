class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def check(a, b):
            while(a > 0):
                rem_a = a % 10
                a //= 10
                if rem_a == 0:
                    return False
            
            while(b > 0):
                rem_b = b % 10
                if rem_b == 0:
                    return False
                
                b //= 10
            
            return True

        a, b = 1, n - 1
        while(True):
            if (a + b) == n and check(a, b):
                return [a, b]

            a += 1
            b -= 1
        
        return True
        

        