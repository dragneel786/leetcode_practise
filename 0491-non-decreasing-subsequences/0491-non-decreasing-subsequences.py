class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        def return_seq(i = 0, ans = []):
            if(i == len(nums)):
                val = tuple(ans)
                if(len(ans) >= 2 and val not in seen):
                    seen.add(val)
                    return [ans]
                return []
            
            res = []
            if(not len(ans) or nums[i] >= ans[-1]):
                res.extend(return_seq(i + 1, ans + [nums[i]]))
            
            res.extend(return_seq(i + 1, ans))
            return res
        
        seen = set()
        return return_seq()
            
            
        