class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city = dict()
        for a, b in paths:
            city[b] = city.get(b, 0)
            city[a] = city.get(a, 0) + 1
        
        ans = ''
        for k, v in city.items():
            if(not v):
                ans = k
        
        return ans
        
        