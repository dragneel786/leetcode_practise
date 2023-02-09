class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if(n == 1):
            return
        
        temp = sorted(nums)
        i = j = 0
        k = n - 1
        while(j <= k):
            nums[i] = temp[j]
            if(i + 1 < n):
                nums[i + 1] = temp[k]
            j += 1
            k -= 1
            i += 2
        