class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinct = set(nums)
        for num in nums:
            distinct.add(int(str(num)[::-1]))
        
        return len(distinct)