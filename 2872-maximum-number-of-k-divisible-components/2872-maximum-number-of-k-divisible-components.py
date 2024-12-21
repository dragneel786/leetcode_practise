class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        def create_tree():
            t = defaultdict(list)
            for a, b in edges:
                t[a].append(b)
                t[b].append(a)
            
            root = -1
            for k, v in t.items():
                if len(v) == 2:
                    return t, k
                
                if len(v) == 1:
                    root = k
            
            return t, root
        
        def divs(node, visited = set()):
            nonlocal count
            if node in visited:
                return 0
            
            tot = 0
            visited.add(node)
            for v in tree[node]:
                if v not in visited:
                    tot += divs(v, visited)
                    
            is_div = ((tot + values[node]) % k) == 0
            if is_div:
                count += 1
            
            return 0 if is_div else (tot + values[node])
        
        count = 0
        if len(edges) > 0:
            tree, root = create_tree()
            divs(root)
            return count
        
        return 1