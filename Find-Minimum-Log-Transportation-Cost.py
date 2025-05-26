class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n < m:
            return self.minCuttingCost(m, n, k)
        
        cut_cost = inf
        if n > k:
            for i in range(1, n):
                if (n - i) <= k and i <= k:
                    cut_cost = min(cut_cost, (n - i) * i)
        
        return cut_cost if cut_cost != inf else 0