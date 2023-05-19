class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        parent = {i:2 for i in range(len(graph))}
        parent[0] = -1
        for i in range(len(graph)):
            for node in graph[i]:
                if(parent[i] == parent[node] \
                   and parent[node] != 2):
                    return False
                
                parent[node] = parent[i] * -1
        
        return True
        
                