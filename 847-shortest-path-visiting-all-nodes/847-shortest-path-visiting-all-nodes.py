class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0
        n = len(graph)
        # If 5 nodes ending mask = 11111
        endingMask = (1 << n) - 1
        # Queue = [(node1, mask1), (node2, mask2) ...]
        queue = [(node, 1 << node) for node in range(n)]
        # Set visited not only by nodes but also currentMask, so the visited states = (node, mask)
        visited = set(queue)
        level = 0
        while queue:
            nextQueue = []
            for node, mask in queue:
                for neighbor in graph[node]:
                    nextMask = mask | (1 << neighbor)
                    # End points means we find shortest path
                    if nextMask == endingMask:
                        return level + 1
                    # Append new state to nextQueue, ignores visited
                    if (neighbor, nextMask) not in visited:
                        visited.add((neighbor, nextMask))
                        nextQueue.append((neighbor, nextMask))
            level += 1
            queue = nextQueue