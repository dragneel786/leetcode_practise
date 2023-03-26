class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        
        def longest(node, before, steps = 0):
            nonlocal ans
            if(node == -1):
                return 

            if(node in before):
                ans = max(ans, steps - before[node])
                return

            before[node] = steps
            longest(edges[node], before, steps + 1)
            edges[node] = -1

        ans = -1
        for v in range(len(edges)):
            longest(v, dict())

        return ans

            