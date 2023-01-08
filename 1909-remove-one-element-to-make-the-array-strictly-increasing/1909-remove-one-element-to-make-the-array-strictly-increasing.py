class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def issorted(skip):
            prev = 0 if(skip) else 1
            for i in range(prev + 1, n):
                if(i == skip):
                    continue
                elif(nums[prev] < nums[i]):
                    prev = i
                else:
                    return False

            return True


        n = len(nums)
        for i in range(1, len(nums)):
            if(nums[i - 1] >= nums[i]):
                j = i
                break

        return i == n - 1 or issorted(j) or issorted(j - 1)
        
                
                    