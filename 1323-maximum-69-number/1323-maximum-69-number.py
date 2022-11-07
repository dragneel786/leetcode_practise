class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        for i, c in enumerate(num):
            if(c == '6'):
                num[i] = '9'
                break
            
        return int(''.join(num))