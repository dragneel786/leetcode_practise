class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        
        def func(n):
            if(n == 1):
                return [0, 1]
            
            perm = func(n - 1)
            power = 2 ** (n - 1)
            return perm + [power + t for t in perm[::-1]]
        
        
        sub_res = func(n)
        idx = sub_res.index(start)
        return sub_res[idx:] + sub_res[:idx]
            
            
            
            
        