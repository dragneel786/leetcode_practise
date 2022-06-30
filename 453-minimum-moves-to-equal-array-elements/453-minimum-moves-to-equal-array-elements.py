class Solution:
    def minMoves(self, nums: List[int]) -> int:
        s = min(nums)
        moves = 0
        for v in nums:
            moves += (v - s)
        return moves