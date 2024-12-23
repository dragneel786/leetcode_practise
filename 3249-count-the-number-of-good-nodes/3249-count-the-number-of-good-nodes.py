class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        
        def get_nodes(node, parent = -1):
            nonlocal ans
            if len(tree[node]) == 1 and parent in tree[node]:
                ans += 1
                return 1
            
            counts = Counter()
            for v in tree[node]:
                if v != parent:
                    counts[v] = get_nodes(v, node)
            
            if len(set(counts.values())) == 1:
                ans += 1
            
            return sum(counts.values()) + 1
            
            
            
        ans = 0
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        get_nodes(0)
        return ans