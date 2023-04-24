class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        
        def delta(node):
            nodi = graph[node]
            size = len(nodi)
            if(not size):
                return [None, None]
            if(size < 2):
                nodi.append(None)
                return nodi
            return nodi
                 

        def create_graph():
            g = defaultdict(list)
            for i, p in enumerate(parents):
                g[p].append(i)
            return g
                
    
        def nodes(node):
            nonlocal high, tot, n
            if(node is None):
                return 0
            
            v_node = delta(node)
            # v_node = [None, None]

            left = nodes(v_node[0])                                   
            right = nodes(v_node[1])
            val = empty(left) * empty(right) * empty(n - left - right - 1)
            if(val > high):
                high = val
                tot = 1
            elif(val == high):
                tot += 1
            
            return left + right + 1
            
        n = len(parents)
        empty = lambda a: a if(a) else 1
        high = tot = 0
        graph = create_graph()

        nodes(0)
        return tot
        
        