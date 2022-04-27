class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        s = list(s)
        visited = [False for _ in range(n)]
        graph = dict()
        for p in pairs:
            if(p[0] not in graph):
                graph[p[0]] = set()
            if(p[1] not in graph):
                graph[p[1]] = set()
            graph[p[0]].add(p[1])
            graph[p[1]].add(p[0])


        for k in graph.keys():
            if(visited[k]):
                continue
            ind = []
            letter = []
            st = deque()
            st.append(k)
            while(len(st)):
                i = st.pop()
                if(visited[i]):
                    continue
                ind.append(i)
                letter.append(s[i])
                visited[i] = True
                for v in graph.get(i, set()):
                    if(not visited[v]):
                        st.append(v)

            ind.sort()
            letter.sort()
            for j in range(len(ind)):
                s[ind[j]] = letter[j]
                
        return "".join(s)