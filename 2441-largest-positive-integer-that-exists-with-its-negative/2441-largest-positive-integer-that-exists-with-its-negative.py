class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        arr = [0] * 2001
        maxv = -1
        for num in nums:
            if(arr[-num + 1000]):
                maxv = max(maxv, abs(num))
            arr[num + 1000] += 1
        
        return maxv