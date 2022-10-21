class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nset = set()
        for i, num in enumerate(nums):
            if(num in nset):
                return True
            nset.add(num)
            
            if(len(nset) > k):
                nset.remove(nums[i - k])
            
        return False
            
            
                