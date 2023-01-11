class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        def create_tree():
            tree = defaultdict(list)
            for a, b in edges:
                tree[a].append(b)
                tree[b].append(a)
            
            return tree
    
        
        def compute(s = 0, visited = set([0])):
            nonlocal ans
            t = 0
            visited.add(s)
            
            for v in tree[s]:
                if(v not in visited):
                    t += (2 * compute(v, visited))
                    
            visited.remove(s)
            ans += t
            return hasApple[s] or t > 0
        
        tree = create_tree()
        ans = 0
        compute()
        return ans