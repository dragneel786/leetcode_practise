class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        def make_graph():
            g = defaultdict(list)
            for n1, n2, d in edges:
                g[n1].append([n2, d])
                g[n2].append([n1, d])

            return g

        def dijK(src, graph, dist):
            dist[src] = 0
            heap = [[0, src]]
            while len(heap) > 0:
                dis, node = heappop(heap)
                for nd, dt in graph[node]:
                    if (dt + dis) < dist[nd]:
                        dist[nd] = dt + dis
                        heappush(heap, [dist[nd], nd])

            return dist

        graph = make_graph()
        res_node, reachable = 0, inf
        for i in range(n):
            dist = [inf] * n
            dijK(i, graph, dist)
            count = 0
            for d in dist:
                count += d <= distanceThreshold
            
            count -= 1
            if count <= reachable:
                reachable = count
                res_node = max(res_node, i)


        return res_node

