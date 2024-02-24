class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def create_graph(meetings):
            g = defaultdict(list)
            for x, y, time in meetings:
                g[x].append((y, time))
                g[y].append((x, time))
            
            return g
        
        graph = create_graph(meetings)
        heap = [(0, 0), (0, firstPerson)]
        ans = set([0])
        max_time = 0
        while(heap):
            ptime, person = heappop(heap)
            max_time = max(ptime, max_time)
            ans.add(person)
            for ns, time in graph[person]:
                if(ns not in ans and max_time <= time):
                    heappush(heap, (time, ns))
                    
        return list(ans)
            