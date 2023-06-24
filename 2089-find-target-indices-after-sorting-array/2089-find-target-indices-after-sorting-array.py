class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()
        idx1 = bisect_left(nums,target)
        idx2 = bisect_right(nums,target)
        if(idx1 == len(nums) or nums[idx1] != target):
            return []
        return range(idx1, idx2)