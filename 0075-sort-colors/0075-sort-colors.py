class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(red, blue, i):
            if(i >= red and nums[i] == 0):
                nums[red], nums[i] = nums[i], nums[red]

            if(i <= blue and nums[i] == 2):
                nums[blue], nums[i] = nums[i], nums[blue]
        
        n = len(nums)
        i = red = 0
        blue = n - 1
        
        while(i < n):
            while(red < n and nums[red] == 0):
                red += 1
            
            while(blue > 0 and nums[blue] == 2):
                blue -= 1
            
            swap(red, blue, i)
            swap(red, blue, i)
            i += 1
        
        