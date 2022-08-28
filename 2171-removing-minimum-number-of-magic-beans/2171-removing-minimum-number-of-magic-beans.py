class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        # 1, 4, 5, 6
        # 2, 2, 3, 10
        beans.sort()
        prefix_sum = [0]
        n = len(beans)
        min_value = lambda idx, bean: prefix_sum[-1] - (bean * (n - idx))
        
        for b in beans:
            prefix_sum.append(prefix_sum[-1] + b)
        
        min_cost = inf
        for i, b in enumerate(beans):
            min_cost = min(min_cost, min_value(i, b))
        
        return min_cost
        
        
        
            
        
        