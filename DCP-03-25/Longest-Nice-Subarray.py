class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        def is_invalid():
            nonlocal map
            for m in map:
                if m > 1:
                    return True
            return False
            
        def ops(o, val):
            nonlocal map
            idx = 0
            while(val):
                map[idx] += o if val & 1 == 1 else 0
                val >>= 1
                idx += 1


        def perform():
            nonlocal start, end, map
            while(start < end and is_invalid()):
                ops(-1, nums[start])
                start += 1

        long = start = 0
        map = [0] * 32
        for end, num in enumerate(nums):
            ops(1, num)
            perform() 
            long = max(end - start + 1, long)

        return long




