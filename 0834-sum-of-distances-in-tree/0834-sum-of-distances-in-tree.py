class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
    
    
        node_count = [1] * n
        ans = [0] * n
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(curr = 0, parent = None):
            for child in graph[curr]:
                if(child != parent):
                    dfs(child, curr)
                    node_count[curr] += node_count[child]
                    ans[curr] += ans[child] + node_count[child]
        
        def dfs2(curr = 0, parent = 0):
            for child in graph[curr]:
                if(child != parent):
                    ans[child] = ans[curr] - node_count[child]\
                    + (n - node_count[child])
                    dfs2(child, curr)
        
        dfs()
        dfs2()
        return ans