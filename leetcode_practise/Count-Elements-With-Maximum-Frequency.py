class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_freq = max_count = 0
        for v in Counter(nums).values():
            if max_freq < v:
                max_freq = v
                max_count = 0
            
            max_count += max_freq == v

        return max_count * max_freq
