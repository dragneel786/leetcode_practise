class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def get_min_and_inc():
            min_sum = inf
            idx = 0
            increase = True
            for j in range(len(nums) - 1):
                increase = increase and nums[j] <= nums[j + 1]
                if min_sum > nums[j] + nums[j + 1]:
                    idx = j
                    min_sum = nums[j] + nums[j + 1]
            
            return increase, idx

        is_inc, i = get_min_and_inc()
        steps = 0
        while(not is_inc):
            nums = nums[:i] + [nums[i] + nums[i + 1]] + nums[i + 2:]
            is_inc, i = get_min_and_inc()
            # print(nums)
            steps += 1
        
        return steps
                
