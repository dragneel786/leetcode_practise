class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def createGraph():
            graph = defaultdict(list)
            for m in meetings:
                x, y, t = m
                graph[x].append((y, t))
                graph[y].append((x, t))
            return graph
        
        def bfs():
            res = set()
            q = [(0, 0), (0, firstPerson)]
            heapify(q)
            while(q):
                if(len(res) == n):
                    return res
                t, p = heappop(q)
                if(p in res):
                    continue
                res.add(p)
                for px, tx in graph[p]:
                    if(px not in res and t <= tx):
                        heappush(q, (tx, px))
            return res
            
        graph = createGraph()
        return bfs()
    
            