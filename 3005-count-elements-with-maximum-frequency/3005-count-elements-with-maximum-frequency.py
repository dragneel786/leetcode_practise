class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_freq = fcount = 0
        for v in counts.values():
            if(v < max_freq):
                continue
            
            if(v > max_freq):
                max_freq = v
                fcount = 0
            
            fcount += max_freq == v
        
        return max_freq * fcount
            
            
            