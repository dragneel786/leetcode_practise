class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        val = sum(nums[:2])
        op = 1
        for i in range(3, len(nums), 2):
            new_tot = nums[i] + nums[i - 1]
            if(new_tot != val):
                break
            
            op += 1

        return op