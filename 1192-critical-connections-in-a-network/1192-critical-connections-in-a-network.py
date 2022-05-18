class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(lambda:[])
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])
        
        dis = [-1] * n
        low = [-1] * n
        parent = [-1] * n
        crit = []
        
        def dfs(v, time = [0]):
            if(dis[v] != -1):
                return
            
            dis[v] = time[0]
            low[v] = time[0]
            time[0] += 1
            for node in graph[v]:
                if(dis[node] == -1):
                    parent[node] = v
                    dfs(node, time)
                    low[v] = min(low[v], low[node])
                    
                    if(low[node] > dis[v]):
                        crit.append([v, node])
                else:
                    if(node != parent[v]):
                        low[v] = min(low[v], dis[node])
                    
        
        for i in range(n):
            if(dis[i] == -1):
                dfs(i)
        return crit