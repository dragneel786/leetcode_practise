class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        def is_corrupt():
            for v in arr:
                if v > 1:
                    return True
            
            return False

        def perform(op, val):
            nonlocal arr
            idx = 0
            while(val):
                if val & 1: arr[idx] += op
                val >>= 1
                idx += 1

        arr = [0] * 32
        max_size = start = 0
        for end, num in enumerate(nums):
            perform(1, num)
            while(is_corrupt()):
                perform(-1, nums[start])
                start += 1
            
            max_size = max((end - start + 1), max_size)
        
        return max_size

            


