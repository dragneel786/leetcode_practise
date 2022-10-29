class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        
        indices = sorted(range(len(plantTime)),\
                          key=lambda i: -growTime[i])
        
        ans = 0
        curr_time = 0
        for i in indices:
            curr_time += plantTime[i]
            ans = max(ans, curr_time + growTime[i])
        
        return ans
            