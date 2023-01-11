class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        def create_tree():
            tree = defaultdict(list)
            for a, b in edges:
                tree[a].append(b)
                tree[b].append(a)
            return tree
    
        
        def compute(s = 0, visited = set([0])):
            t = 0
            visited.add(s)
            
            for v in tree[s]:
                if(v not in visited):
                    t += compute(v, visited)
                    
            visited.remove(s)
            return (2 * (hasApple[s] or t > 0)) + t
        
        tree = create_tree()
        return max(compute() - 2, 0)