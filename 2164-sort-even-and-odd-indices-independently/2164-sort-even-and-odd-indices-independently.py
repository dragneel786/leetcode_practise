class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:        
        def sort2(start, condt):
            n = len(nums)
            for i in range(start, n, 2):
                for j in range(start, n - 2, 2):
                    if(condt(nums[j], nums[j + 2])):
                        nums[j + 2], nums[j] =\
                        nums[j], nums[j + 2]
                    
        cond1 = lambda x, y: x >= y
        cond2 = lambda x, y: x <= y
        sort2(0, cond1)
        sort2(1, cond2)
        return nums
            