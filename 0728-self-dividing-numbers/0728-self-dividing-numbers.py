class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        def is_div():
            for num in range(left, right + 1):
                temp = num
                while(temp):
                    mod = temp % 10
                    if(not mod or num % mod):
                        break
                    temp //= 10
                else:
                    yield num
        
        return [i for i in is_div()]
        
            