class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        def create_graph():
            g = defaultdict(list)
            for i, route in enumerate(routes):
                for a in route:
                    g[a].append(i)
            return g
        
        graph = create_graph()
        q = deque([source])
        visited_stop = set([source])
        visited_bus = set()
        level = 0
        while(q):
            for _ in range(len(q)):
                stop = q.popleft()
                if(stop == target):
                    return level
                for bus in graph[stop]:
                    if(bus in visited_bus):
                        continue
                        
                    for bus_stop in routes[bus]:
                        if(bus_stop not in visited_stop):
                            q.append(bus_stop)
                            visited_stop.add(bus_stop)
                    
                    visited_bus.add(bus)
            
            level += 1
            
        
        return -1
                    
                    
                
        