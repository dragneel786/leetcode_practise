class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHash = defaultdict(lambda:math.inf)
        minHash[k] = 0
        graph = defaultdict(lambda:[])
        for t in times:
            graph[t[0]].append([t[1], t[2]])
    
        st = deque()
        st.append(k)
        while(len(st)):
            for _ in range(len(st)):
                node = st.pop()
                for v in graph[node]:
                    if(minHash[v[0]] > v[1] + minHash[node]):
                        minHash[v[0]] = v[1] + minHash[node]
                        st.appendleft(v[0])
        val = -math.inf
        for i in range(1, n + 1):
            if(minHash[i] == math.inf):
                return -1
            val = max(minHash[i], val)
                
        return val
            
                    
            
            