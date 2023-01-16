class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i, v in zip(index, nums):
            ans.insert(i, v)
        
        return ans