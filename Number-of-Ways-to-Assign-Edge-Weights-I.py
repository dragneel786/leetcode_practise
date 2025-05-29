class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        def make_tree():
            nonlocal edges
            tree = defaultdict(list)
            for a, b in edges:
                tree[a].append(b)
                tree[b].append(a)

            return tree

        
        def get_max_depth(node, visited):
            if node in visited:
                return 0
            
            max_d = 0
            visited.add(node)
            for nei in tree[node]:
                max_d = max(max_d, get_max_depth(nei, visited))
            visited.remove(node)

            return max_d + 1
            

        tree = make_tree()
        max_depth = get_max_depth(1, set())
        return (2 ** (max_depth - 2)) % (10 ** 9 + 7)

        