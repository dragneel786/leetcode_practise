class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        def make_graph():
            g = defaultdict(list)
            for a, b in edges:
                g[a].append(b)
                g[b].append(a)
            
            return g
        
        size = len(patience)
        graph = make_graph()
        dis = [-1] * size
        dis[0] = 0
        que = deque([0])
        steps = 1
        while(len(que)):
            for _ in range(len(que)):
                e = que.popleft()
                for v in graph[e]:
                    if dis[v] == -1:
                        que.append(v)
                        dis[v] = steps

            steps += 1
        
        ans = 0
        for d, p in zip(dis[1:], patience[1:]):
            td = (d * 2 - 1) // p
            lout = td * p
            ans = max(ans, lout + (d * 2))
        
        return ans + 1
        


        


                

                
            


