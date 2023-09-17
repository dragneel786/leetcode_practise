class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        
        n = len(graph)
        q = deque()
        visited = set()
        for i in range(n):
            state = (i, 1 << i)
            q.append(state)
            visited.add(state)
        
        end_state = (1 << n) - 1
        steps = 0
        while(q):
            for _ in range(len(q)):
                node, state = q.popleft()
                if(state == end_state):
                    return steps
                
                for v in graph[node]:
                    new_state = (v, state | (1 << v))
                    if(new_state not in visited):
                        visited.add(new_state)
                        q.append(new_state)

            steps += 1
            
        
        return steps
        
        
            
        