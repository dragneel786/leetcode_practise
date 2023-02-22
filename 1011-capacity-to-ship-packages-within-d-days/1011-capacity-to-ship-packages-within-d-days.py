class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def isvalid(weight):
            nonlocal days
            day_counts = 0
            curr_wei = 0
            for w in weights:
                if(curr_wei + w > weight):
                    curr_wei = 0
                    day_counts += 1
                
                curr_wei += w
            
            day_counts += (curr_wei > 0)
            return day_counts <= days
                
        
        low = max(weights)
        high = sum(weights)
        ans = 0
        while(low <= high):
            mid = low + (high - low) // 2
            if(isvalid(mid)):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
                
        