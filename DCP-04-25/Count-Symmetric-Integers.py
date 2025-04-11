class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_sym(num):
            num = str(num)
            n = len(num)
            if n & 1:
                return False

            first = second = 0
            for i in range(n//2):
                first += int(num[i])
                second += int(num[n - i - 1])
            
            return first == second

        res = 0
        for val in range(low, high + 1):
            res += is_sym(val)
        
        return res