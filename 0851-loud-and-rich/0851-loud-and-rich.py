class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        def create_graph(richer):
            graph = defaultdict(list)
            for a, b in richer:
                graph[b].append(a)
            
            return graph
        
        
        def dfs(node, visited):
            nonlocal res, qval
            if(node in visited):
                return 
            
            visited.add(node)
            if(quiet[node] <= qval):
                res = node
                qval = quiet[node]
            for v in graph[node]:
                dfs(v, visited)
                
            
        
        n = len(quiet)
        graph = create_graph(richer)
        ans = [0] * n
        for i in range(n):
            res = i
            qval = inf
            dfs(i, set())
            ans[i] = res
        
        return ans
        
                