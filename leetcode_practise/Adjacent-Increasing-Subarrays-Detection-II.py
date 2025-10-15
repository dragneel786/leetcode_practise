class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        max_k = 0
        inc_seq = 0
        curr_seq = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                curr_seq += 1
            else:
                inc_seq = curr_seq
                curr_seq = 1
            
            max_k = max(max_k, max(curr_seq // 2, min(curr_seq, inc_seq)))
        
        return max_k