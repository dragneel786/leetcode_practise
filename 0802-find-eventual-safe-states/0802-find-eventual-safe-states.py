class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def dfs(node, visited):
            if(node in non_res):
                return False
            
            if(node in res):
                return True
            
            if(not graph[node]):
                res.add(node)
                return True
            
            for v in graph[node]:
                if(v in visited):
                    non_res.add(v)
                    return False
                
                visited.add(v)
                if(not dfs(v, visited)):
                    non_res.add(v)
                    return False
                visited.remove(v)
                
            res.add(node)
            return True
        
        res = set()
        non_res = set()
        for i in range(len(graph)):
            if(dfs(i, set([i]))):
                res.add(i)
            else:
                non_res.add(i)
        
        return sorted(list(res))