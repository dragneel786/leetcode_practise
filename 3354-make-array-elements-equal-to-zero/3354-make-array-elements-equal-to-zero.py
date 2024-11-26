class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        sums = sum(nums)
        curr_tot = 0
        counts = 0
        for num in nums:
            curr_tot += num
            sums -= num
            if num == 0:
                counts += (2 * (curr_tot == sums)) + (1 * (curr_tot + 1 == sums)) + (1 * (curr_tot == sums + 1))
        
        
        return counts