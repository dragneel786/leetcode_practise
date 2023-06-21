class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        def calcy(med):
            ans = 0
            for a, b in li:
                ans += abs(a - med) * b
            return ans
        
        li = [[a, b] for a, b in zip(nums, cost)]
        li.sort()
        
        cost_sum = sum(cost)
        median = tot = i = 0
        n = len(nums)
        while(tot < (cost_sum + 1) / 2 and i < n):
            tot += li[i][1]
            median = li[i][0]
            i += 1
        
        return calcy(median)
            