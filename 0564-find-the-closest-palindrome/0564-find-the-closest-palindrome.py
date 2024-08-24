class Solution:
    def nearestPalindromic(self, n: str) -> str:
        
        def get_palindrome(left, is_even):
            res = left
            if not is_even: 
                left //= 10
            
            while(left > 0):
                res = (res * 10) + (left % 10)
                left //= 10
            
            return res
        
        nsize = len(n)
        half_size = nsize // 2 - 1 if nsize % 2 == 0 else nsize // 2
        half_num = int(n[:half_size + 1])
        possibles = []
        possibles.append(get_palindrome(half_num, nsize % 2 == 0))
        possibles.append(get_palindrome(half_num + 1, nsize % 2 == 0))
        possibles.append(get_palindrome(half_num - 1, nsize % 2 == 0))
        possibles.append(10 ** nsize + 1)
        possibles.append(10 ** (nsize - 1) - 1)
        
        num = int(n)
        diff = inf
        print(possibles)
        ret = 0
        for val in possibles:
            abs_diff = abs(num - val)
            if val == num:
                continue
                
            if abs_diff < diff:
                ret = val
                diff = abs_diff
            
            if abs_diff == diff:
                ret = min(val, ret)
        
        
        return str(ret)