class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        mid = 0
        moves = 0
        if(n & 1):
            mid = nums[n // 2]
        else:
            mid = (nums[n // 2] + nums[n // 2 - 1]) // 2
        
        for n in nums:
            moves += abs(mid - n)
    
        return moves