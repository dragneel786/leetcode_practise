class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        inc_seq = 0
        curr_seq = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                curr_seq += 1
            else:
                inc_seq = curr_seq
                curr_seq = 1
            
            # print(inc_seq, curr_seq)
            if curr_seq >= (2 * k) or (inc_seq >= k and curr_seq >= k):
                return True
        
        return False
            


