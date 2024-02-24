class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        def create_graph(meetings):
            g = defaultdict(list)
            for x, y, time in meetings:
                g[x].append((y, time))
                g[y].append((x, time))
            
            return g
        
        graph = create_graph(meetings)
        earliest = [inf] * n
        earliest[0] = 0
        earliest[firstPerson] = 0
        
        q = deque([(0, 0), (0, firstPerson)])
        ans = set()
        while(q):
            ptime, person = q.popleft()
            ans.add(person)
            for ns, time in graph[person]:
                if(time >= ptime and earliest[ns] > time):
                    q.append((time, ns))
                    earliest[ns] = time
                    
        return list(ans)
            