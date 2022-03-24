class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        seen = defaultdict(lambda:0)
        for p in people:
            seen[p] += 1
        
        boats = 0
        for p in people:
            if(not seen[p]):
                continue
            
            seen[p] -= 1
            val = limit - p
            while(not seen[val] and val):
                val -= 1
            
            if(seen[val]):
                seen[val] -= 1
            
            boats += 1
        
        return boats