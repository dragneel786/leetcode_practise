class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        def return_seq(i = 0, ans = []):
            if(i == len(nums)):
                if(len(ans) >= 2):
                    result.add(tuple(ans))
                return
            
            if(not len(ans) or nums[i] >= ans[-1]):
                return_seq(i + 1, ans + [nums[i]])
            return_seq(i + 1, ans)
        
        result = set()
        return_seq()
        return result
            
            
        