class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1

        nums.sort()
        nums = list(set(nums))
        max_till = nums[0] * dic[nums[0]]
        max_before = 0
        for i in range(1, len(nums)):
            temp = 0
            val = nums[i] * dic[nums[i]]
            if(nums[i] - 1 == nums[i - 1]):
                temp = max_before + val
            else:
                temp = max_till + val

            max_before = max_till
            max_till = max(max_till, temp)

        return max_till