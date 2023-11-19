class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def get_happy_string(st = ''):
            nonlocal curr_ith
            if(len(st) == n):
                curr_ith += 1
                if(curr_ith == k):
                    return st
                
                return ''
            
            for c in ['a', 'b', 'c']:
                if(len(st) == 0 or st[-1] != c):
                    val = get_happy_string(st + c)
                    if(len(val) != 0):
                        return val
            
            return ''
                    
        curr_ith = 0
        return get_happy_string()