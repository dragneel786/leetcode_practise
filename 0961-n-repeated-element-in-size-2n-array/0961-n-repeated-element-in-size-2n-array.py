class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        occured = set()
        for num in nums:
            if(num in occured):
                return num
            occured.add(num)
        