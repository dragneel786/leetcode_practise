class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        
        left_cap = [c - r for c, r in zip(capacity, rocks)]
        left_cap.sort()
        
        full_count = 0
        for c in left_cap:
            if(c > additionalRocks):
                break
            additionalRocks -= c
            full_count += 1
        
        return full_count
            