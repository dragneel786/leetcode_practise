class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        
        def check_sorted(i):
            prev = 0
            for a in nums[i:] + nums[:i]:
                if(prev > a):
                    return -1
                prev = a
            return i
                
        n = len(nums)
        for i in range(1, n):
            if(nums[i] < nums[i - 1]):
                ret = check_sorted(i)
                return n - ret if(ret != -1) else ret

        return 0
        