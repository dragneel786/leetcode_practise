class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ops = 0
        heapify(nums)
        while(len(nums) > 1 and nums[0] < k):
            a, b = heappop(nums), heappop(nums)
            heappush(nums, a * 2 + b)
            ops += 1
        
        return ops
            