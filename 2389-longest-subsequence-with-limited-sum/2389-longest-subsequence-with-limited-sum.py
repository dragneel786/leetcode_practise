class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        tot = 0
        ans = [0] * len(queries)
        for i, num in enumerate(nums):
            tot += num
            for i, q in enumerate(queries):
                if(tot <= q):
                    ans[i] += 1
            
        
        return ans