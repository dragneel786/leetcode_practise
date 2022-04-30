class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(lambda:[])
        for i in range(len(values)):
            graph[equations[i][0]]\
                .append((equations[i][1], values[i]))
            graph[equations[i][1]]\
                .append((equations[i][0], 1/values[i]))

        def bfs(start, end):
            st = deque()
            visited = set()
            st.append((start, 1))
            while(len(st)):
                for _ in range(len(st)):
                    node = st.pop()
                    if(node[0] == end):
                        return node[1]
                    if(node[0] in visited):
                        continue
                    visited.add(node[0])
                    for v in graph[node[0]]:
                        st.appendleft((v[0], node[1] * v[1]))

            return -1



        res = []
        for q in queries:
            if(graph[q[0]] and graph[q[1]]):
                res.append(bfs(*q))
            else:
                res.append(-1)

        return res