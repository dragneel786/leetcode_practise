class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        vals = sorted(nums)
        s = Counter(vals[-k:])
        ans = []
        for num in nums:
            if(s[num]):
                ans.append(num)
                s[num] -= 1
        
        return ans