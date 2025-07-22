class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start = max_tot = tot = 0
        counts = Counter()
        for end, num in enumerate(nums):
            tot += num
            counts[num] += 1
            while(start < end and counts[num] >= 2):
                tot -= nums[start]
                counts[nums[start]] -= 1
                start += 1
            
            max_tot = max(max_tot, tot)
        
        return max_tot
