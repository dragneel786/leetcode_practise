class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = Counter(nums)
        for k in seen.keys():
            if(seen[k] > 1):
                return True
        return False