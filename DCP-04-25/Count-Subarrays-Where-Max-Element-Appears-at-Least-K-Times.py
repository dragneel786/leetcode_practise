class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = start = counts = 0
        max_val = max(nums)
        for end in range(len(nums)):
            counts += nums[end] == max_val

            while(start < end):
                if (counts - (nums[start] == max_val)) < k:
                    break
                counts -= nums[start] == max_val
                start += 1
            
            # print(nums[start: end + 1])
            if counts == k:
                res += start + 1
        
        return res
