class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        negi, posi = 1, 0
        for num in nums:
            if(num < 0):
                res[negi] = num
                negi += 2
            else:
                res[posi] = num
                posi += 2
            
        return res
            