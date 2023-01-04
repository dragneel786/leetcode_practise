class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq_val = Counter(tasks).values()
        # if(1 in freq_val):
        #     return -1
        
        ans = 0
        for f in freq_val:
            if(f == 1):
                return -1
            
            ans += (f // 3)
            if(f % 3):
                ans += 1
        
        return ans
                
        
        
        
        
                
        
        
        