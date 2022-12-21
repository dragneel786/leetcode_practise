class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        def create_graph():
            graph = defaultdict(list)
            for a, b in dislikes:
                graph[a].append(b)
                graph[b].append(a)

            return graph


        def bfs(s):
            q = deque([s])

            while(q):
                node = q.popleft()
                for v in dgraph[node]:
                    if(colors[v] == -1):
                        colors[v] = 1 - colors[node]
                        q.append(v)

                    elif(colors[v] == colors[node]):
                        return False

            return True

        colors = [-1] * (n + 1)
        dgraph = create_graph()

        for i in range(1, n + 1):
            if(i in dgraph and colors[i] == -1):
                colors[i] = 1
                if(not bfs(i)):
                    return False

        return True
