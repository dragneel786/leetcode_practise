class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def isvalid(num, val, idx):
            if(num and \
               ((num % 10 > val and pattern[idx] == "I")\
                or (num % 10 < val and pattern[idx] == "D"))):
                return False
            
            return True
            
               
        def create_pattern(num = 0,\
                           j = -1,\
                           options = set([1,2,3,4,5,6,7,8,9])):        
            if(j == len(pattern)):
                return str(num)
            
            minv = "999999999"
            for v in options:
                if(isvalid(num, v, j)):
                    minv = min(minv, create_pattern(\
                        num * 10 + v, j + 1, options - {v}))
            return minv
        
        return create_pattern()
                    
                    
                    