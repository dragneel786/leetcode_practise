class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def combine(remain = target):
            if(remain <= 0):
                return remain == 0

            tot = 0
            for num in nums:
                tot += combine(remain - num)

            return tot


        nums.sort()
        if(nums[0] > target):
            return 0

        return combine()
                
        
        
        