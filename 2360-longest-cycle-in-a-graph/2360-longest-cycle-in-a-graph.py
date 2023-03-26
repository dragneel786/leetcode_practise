class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        def longest(node, before, steps = 0):
            if(node == -1):
                return 

            if(node in before):
                visited[node] = steps - before[node]
                return

            before[node] = steps
            longest(edges[node], before, steps + 1)

        visited = dict()
        for v in range(len(edges)):
            longest(v, dict())
            edges[v] = -1

        return max(visited.values()) if (visited) else -1

            