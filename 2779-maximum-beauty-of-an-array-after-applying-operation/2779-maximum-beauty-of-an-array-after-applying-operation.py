class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        max_w = 0
        for end in range(len(nums)):
            while(start <= end and nums[start] + k < nums[end] - k):
                start += 1
            
            max_w = max(max_w, end - start + 1)
        
        return max_w
        
        
            # 1, 2, 4, 6