class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        def find_combo(i):
            low = 0
            high = i - 1
            ret = events[i][2]
            while(low <= high):
                mid = low + ((high - low) // 2)
                if events[mid][1] < events[i][0]:
                    ret = cost[mid] + events[i][2]
                    low = mid + 1
                else:
                    high = mid - 1
            
            return ret
                
        
        events.sort(key=lambda x: x[1])
        cost = [events[0][2]]
        for i in range(1, len(events)):
            cost.append(max(cost[-1], events[i][2]))
        
        res = events[0][2]
        for i in range(1, len(events)):
            res = max(res, find_combo(i))
        
        return res
            