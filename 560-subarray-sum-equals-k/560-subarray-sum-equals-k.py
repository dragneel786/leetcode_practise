class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        seen = defaultdict(int)
        prefix = [nums[0]]
        for i in range(1, n):
            prefix.append(prefix[-1] + nums[i])

        count = 0
        for i in range(len(nums)):
            if(prefix[i] == k):
                count += 1
            if(prefix[i] - k in seen):
                count += seen[prefix[i] - k]
            seen[prefix[i]] += 1

        return count