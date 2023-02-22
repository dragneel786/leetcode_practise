class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        
        options = "123456789"
        used = set()
        
        def isvalid(num, val, idx):
            nonlocal options
            if(num and \
               ((num % 10 > val and pattern[idx] == "I")\
                or (num % 10 < val and pattern[idx] == "D"))):
                return False
            
            return True
            
               
        def create_pattern(num=0, j = -1):
            nonlocal options
            # print(num, j)
            if(j == len(pattern)):
                return str(num)
            
            minv = "999999999"
            for i in range(9):
                if(options[i] not in used and\
                   isvalid(num, int(options[i]), j)):
                    used.add(options[i])
                    minv = min(minv, create_pattern(\
                        num * 10 + int(options[i]), j + 1))
                    used.discard(options[i])
            return minv
        
        return create_pattern()
                    
                    
                    