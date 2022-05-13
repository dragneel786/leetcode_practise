class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        i, j = 0, n - 1
        while(i <= j):
            if(nums[i] + nums[j] <= target):
                count += 1 << (j - i)
                i += 1
            else:
                j -= 1
        
        return count % (10 ** 9 + 7)
                
            
            