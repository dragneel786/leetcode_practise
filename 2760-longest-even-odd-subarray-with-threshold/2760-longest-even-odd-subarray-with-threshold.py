class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        start = -1
        max_len = 0
        is_even = True
        valid = lambda state, num: (state == (num % 2 == 0)\
                                    and num <= threshold)
        nums.append(nums[-1])
        
        for end, num in enumerate(nums):
            if(valid(is_even, num)):
                if(start == -1):
                    start = end
                
                is_even = not is_even
            else:
                print(is_even, start, end, max_len)
                if(start != -1):
                    max_len = max(end - start, max_len)
                is_even = False if(valid(True, num)) else True
                start = end if(valid(True, num)) else -1
                # print(is_even, start, end, max_len)
                
        return max_len
            
            
                
        
            