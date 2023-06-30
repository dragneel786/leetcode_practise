class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        counts = Counter()
        ans = freq = 0
        for i in range(1, len(nums)):
            if(nums[i - 1] == key):
                counts[nums[i]] += 1
            
            if(freq < counts[nums[i]]):
                ans = nums[i]
                freq = counts[nums[i]]
        
        return ans
            