class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def union(parents, x, y):
            px, py = find(parents, x), find(parents, y)
            if(px != py):
                parents[py] = px
            
            return px == py
        
        def find(parents, x):
            if(parents[x] != x):
                parents[x] = find(parents, parents[x])
            
            return parents[x]
        
        def reachable(graph):
            prev = find(graph, 1)
            for i in range(2, n + 1):
                if(prev != find(graph, i)):
                    return False
            
            return True
        
        alice = {i:i for i in range(1, n + 1)}
        bob = {i:i for i in range(1, n + 1)}
        edges.sort(reverse=True)
        deleted = 0
        
        for edge_type, a, b in edges:
            if(edge_type == 3):
                deleted += union(alice, a, b) == \
                union(bob, a, b) == True
            elif(edge_type == 2):
                deleted += union(bob, a, b)
            else:
                deleted += union(alice, a, b)
        
        if(not reachable(alice) or not reachable(bob)):
            print(alice, bob)
            return -1
        
        return deleted
        
            