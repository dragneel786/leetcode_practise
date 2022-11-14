class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        def group():
            hash_set = defaultdict(list)
            for i, (x, y) in enumerate(stones):
                hash_set['r' + str(x)].append(i)
                hash_set['c' + str(y)].append(i)
            
            return hash_set
        
        
        def create_graph(groups):
            ret = defaultdict(set)
            for _, v in groups.items():
                for node in v:
                    ret[node].update(v)
                    ret[node].discard(node)
            
            return ret
        
        
        def dfs(curr, visited):
            visits = 0
            
            for node in graph[curr]:
                if(node not in visited):
                    visited.add(node)
                    visits += (dfs(node, visited) + 1)
            
            graph[curr].clear()
            return visits
        
        graph = create_graph(group())
        deleted = 0
        for i in range(len(stones)):
            if(graph[i]):
                deleted += dfs(i, set([i]))
        
        return deleted