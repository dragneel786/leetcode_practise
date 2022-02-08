class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1

        nums = list(set(nums))
        nums.sort()
        max_till = nums[0] * dic[nums[0]]
        max_before = 0
        for i in range(1, len(nums)):
            temp = 0
            val = (nums[i] * dic[nums[i]])
            if(nums[i - 1] + 1 == nums[i]):
                temp = max_before + val
                # if(temp > max_till):
                #     max_before = max_till
                #     max_till = temp
                # else:
                #     max_before = max_till
            else:
                temp = max_till + val
                # max_before = max_till
                # max_till = temp
            max_before = max_till
            if(temp > max_till):
                max_till = temp

        return max_till