class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        li = [0] * 20010
        for num in nums:
            num += 10000
            li[num] += 1
        
        k = len(nums) - k
        for i in range(20010):
            k -= li[i]
            if(k < 0):
                break
        
        return i - 10000