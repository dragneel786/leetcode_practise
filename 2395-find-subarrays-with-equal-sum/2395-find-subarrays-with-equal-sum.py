class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        nset = set()
        for i in range(len(nums) - 1):
            tot = nums[i] + nums[i + 1]
            if(tot in nset):
                return True
            nset.add(tot)
        
        return False