class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        prev = nums[-1]
        for num in nums[:-1][::-1]:
            if prev < num:
                div = (num + prev - 1) // prev
                ans += (div - 1)
                prev = num // div
            else:
                prev = num
        
        return ans