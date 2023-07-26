class Solution:
    def captureForts(self, forts: List[int]) -> int:
        
        def traverse(itr):
            prev_i = -1
            count = 0
            ans = 0
            for i in itr:
                f = forts[i]
                if(f != 0):
                    if(f == -1):
                        ans = max(count, ans)
                    
                    count = 0
                    prev_i = f

                elif(prev_i != -1):
                    count += 1
            
            return ans
        
        n = len(forts)
        return max(traverse(range(n)),\
                   traverse(range(n - 1, -1,-1)))
            