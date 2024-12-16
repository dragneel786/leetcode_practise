class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        max_val = prev = 0
        idx = inf
        for index, time in events:
            # print(time - prev, index)
            diff = time - prev
            if diff >= max_val:
                if diff == max_val:
                    idx = min(index, idx)
                else:
                    idx = index
                    
                max_val = diff
            
            prev = time
        
        return idx