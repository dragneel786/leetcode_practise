class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(lst = [0]):
            if(lst[-1] == len(graph) - 1):
                return ans.append(lst)
            
            
            for v in graph[lst[-1]]:
                dfs(lst + [v])
        
        ans = []
        dfs()
        return ans
            
            
            
            
            
                    
        