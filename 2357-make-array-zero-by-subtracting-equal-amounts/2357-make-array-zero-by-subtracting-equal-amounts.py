class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        value = count = 0
        for num in nums:
            if(num - value > 0):
                value += (num - value)
                count += 1
        
        return count
            