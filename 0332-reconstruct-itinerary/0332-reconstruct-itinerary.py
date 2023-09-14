class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        def construct_graph():
            g = defaultdict(list)
            for i, (frm, to) in enumerate(tickets):
                g[frm].append((to, i))
            
            for k, v in g.items():
                g[k] = sorted(v)
            
            return g
        
        
        def traverse(nodes, visited = set()):
            if(len(visited) == n):
                return nodes
            
            for node, idx in graph[nodes[-1]]:
                if(idx not in visited):
                    visited.add(idx)
                    ret = traverse(nodes + [node], visited)
                    visited.discard(idx)
                
                    if(ret):
                        return ret
            
            return []
                
        n = len(tickets)
        graph = construct_graph()
        return traverse(["JFK"])
            
            
                
                