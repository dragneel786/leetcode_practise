class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = nums[0] + nums[1] + nums[-1]
        for i in range(n - 2):
            start = i + 1
            end = n - 1
            sumTemp = 0
            while(start < end):
                sumTemp = nums[i] + nums[start] + nums[end] 
                if(sumTemp > target):
                    end -= 1
                else:
                    start += 1

                if(abs(target - sumTemp) < abs(target - res)):
                    res = sumTemp

        return res