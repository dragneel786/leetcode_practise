class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        ans = []
        for x, y, dis in queries:
            count = 0
            for a, b in points:
                euc_d = sqrt(((a - x) ** 2) + ((b - y) ** 2))
                count += (euc_d <= dis)
        
            ans.append(count)
        
        return ans