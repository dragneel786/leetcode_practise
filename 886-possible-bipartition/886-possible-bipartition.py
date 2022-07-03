class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def find(x):
            if(parent[x] != x):
                parent[x] = find(parent[x])
            return parent[x]
        
        graph = defaultdict(lambda:[])
        for d in dislikes:
            a, b = d
            graph[a].append(b)
            graph[b].append(a)
        
        parent = {i:i for i in range(1, n + 1)}
        for i in range(1, n + 1):
            if(graph[i]):
                p1 = find(i)
                p2 = find(graph[i][0])
                if(p2 == p1): return False
                for v in graph[p1][1:]:
                    op = find(v)
                    if(op == p1): return False
                    parent[op] = p2
        return True
                