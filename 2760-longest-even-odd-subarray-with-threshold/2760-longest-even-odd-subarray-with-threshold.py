class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        start = -1
        max_len = 0
        even = True
        valid = lambda state, num: (state == (num % 2 == 0)\
                                    and num <= threshold)
        nums.append(nums[-1])
        
        for end, num in enumerate(nums):
            if(valid(even, num)):
                if(start == -1):
                    start = end
                even = not even
                continue
                
            if(start != -1):
                max_len = max(end - start, max_len)

            even = True
            start = -1
            if(valid(True, num)):
                even = False
                start = end
                
        return max_len
            
            
                
        
            