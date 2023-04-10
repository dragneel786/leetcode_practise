class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        def create_graph():
            for a, b in edges:
                graph[a].append(b)
                indegree[b] += 1
        
        graph = defaultdict(list)
        indegree = Counter()
        create_graph()
        
        n = len(colors)
        q = deque()
        for i in range(n):
            if(not indegree[i]):
                q.append(i)
        
        seen = 0
        max_color = 0
        color_counts = [([0] * 26) for _ in range(n)]
        while(q):
            node = q.popleft()
            color_idx = ord(colors[node]) - 97
            color_counts[node][color_idx] += 1
            max_color = max(max_color, color_counts[node][color_idx])
            
            for v in graph[node]:
                for i in range(26):
                    color_counts[v][i] = max(color_counts[v][i],\
                                             color_counts[node][i])
                    
                indegree[v] -= 1
                if(indegree[v] <= 0):
                    q.append(v)

            
            seen += 1
        
        return max_color if(seen >= n) else -1
            
            