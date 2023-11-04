class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            num = str(num)
            n = len(num)
            if(n % 2 == 0):
                left = reduce(lambda a, b: int(a) + int(b),\
                              list(num[:n // 2]))
                right = reduce(lambda a, b: int(a) + int(b),\
                               list(num[n // 2:]))
                count += left == right
    
        return count
                
                