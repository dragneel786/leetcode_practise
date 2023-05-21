class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        def valid_code(added = {0, 1}):
            if(len(ans) == 2 ** n):
                return True
            
            for i in range(2 ** n):
                val = ans[-1] ^ i
                if(val not in added):
                    added.add(val)
                    ans.append(val)
                    if(valid_code(added)):
                        return True
                    added.discard(val)
                    ans.pop()
            
            return False
                    
            
        ans = [0, 1]
        valid_code()
        return ans
        