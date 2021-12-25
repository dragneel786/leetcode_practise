class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 1):
            return nums[0]

        bt = nums[0]
        bw = 0
        for i in range(1, n):
            val = bw + nums[i]
            if(val > bt):
                bw = bt
                bt = val
            else:
                bw = bt

        return bt