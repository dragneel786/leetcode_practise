class Solution:
    def captureForts(self, forts: List[int]) -> int:
        index_one = -1
        index_none = -1
        ans = 0
        for i, f in enumerate(forts):
            if(f == 1):
                if(index_none != -1):
                    ans = max(ans, i - index_none - 1)
                
                index_one = i
                index_none = -1
            
            elif(f == -1):
                if(index_one != -1):
                    ans = max(ans, i - index_one - 1)
                
                index_none = i
                index_one = -1
        
        return ans
                
            