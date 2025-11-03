class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i, n = 0, len(colors)
        ans = 0
        while (i < n - 1):
            sums = max_val = neededTime[i]
            j = i + 1
            while (j < n and colors[j] == colors[i]):
                sums += neededTime[j]
                max_val = max(max_val, neededTime[j])
                j += 1

            if (j - i > 1):
                ans += sums - max_val

            i = j
        
        return ans
            
            
                
            