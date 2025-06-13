class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapify(nums)
        tot = 0
        for _ in range(k):
            val = -heappop(nums)
            tot += val
            heappush(nums, -ceil(val/3))
        
        return tot
        
            
            
        