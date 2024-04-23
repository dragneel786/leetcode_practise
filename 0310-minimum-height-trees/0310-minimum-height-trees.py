class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if(n < 3):
            return [i for i in range(n)]
        
        tree = [set() for _ in range(n)]
        for a, b in edges:
            tree[a].add(b)
            tree[b].add(a)
            
        leaves = deque([a for a in range(n) if(len(tree[a]) == 1)])
        
        remain_nodes = n
        while(remain_nodes > 2):
            remain_nodes -= len(leaves)
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                neigh = tree[leaf].pop()
                tree[neigh].remove(leaf)
                
                if(len(tree[neigh]) == 1):
                    leaves.append(neigh)
        
        return leaves