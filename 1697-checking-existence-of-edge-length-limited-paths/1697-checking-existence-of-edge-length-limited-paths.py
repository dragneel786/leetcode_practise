class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        def union(x, y):
            px, py = find(x), find(y)
            if(px != py):
                parents[py] = px
        
        
        def find(x):
            if(parents[x] != x):
                parents[x] = find(parents[x])
            
            return parents[x]
        
        
        parents = {i:i for i in range(n)}
        queries_index = [[*q, i] for i, q in enumerate(queries)]  
        queries_index.sort(key=lambda x: x[2])
        edgeList.sort(key=lambda x: x[2])
        ans = [False] * len(queries)
        eid = 0
        
        for a, b, lim, idx in queries_index:
            
            while(eid < len(edgeList) and edgeList[eid][2] < lim):
                x, y, _ = edgeList[eid]
                union(x, y)
                eid += 1
            
            if(find(a) == find(b)):
                ans[idx] = True
        
        return ans
        