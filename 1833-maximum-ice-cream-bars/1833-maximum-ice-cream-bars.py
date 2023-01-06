class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        m = max(costs) + 1
        cmap = [0] * m
    
        for c in costs:
            cmap[c] += 1
        
        ans = 0
        for i in range(1, m):
            if(i > coins):
                break
            
            ans += min(cmap[i], coins // i)
            coins -= cmap[i] * i
        
        return ans
                