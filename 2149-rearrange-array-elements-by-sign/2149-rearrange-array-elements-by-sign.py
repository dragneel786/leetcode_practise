class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new_list = [0] * n
        pos = 0
        neg = 1
        for num in nums:
            if(num < 0):
                new_list[neg] = num
                neg += 2
            
            else:
                new_list[pos] = num
                pos += 2
        
        return new_list