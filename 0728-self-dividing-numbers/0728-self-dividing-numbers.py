class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        def is_div(num):
            temp = num
            while(temp):
                mod = temp % 10
                temp //= 10
                if(not mod or num % mod):
                    return False
            return True
        
        return filter(is_div, range(left, right + 1))
        
            