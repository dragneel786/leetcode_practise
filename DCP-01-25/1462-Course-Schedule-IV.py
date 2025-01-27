class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def make_graph():
            d = defaultdict(list)
            in_degree = [0] * numCourses 
            for a, b in prerequisites:
                d[a].append(b)
                in_degree[b] += 1

            return d, in_degree 
        
        graph, in_degree = make_graph()
        q = deque()
        for i, v in enumerate(in_degree):
            if v == 0:
                q.append(i)
        
        index_set = {i: set() for i in range(numCourses)}
        while(q):
            for _ in range(len(q)):
                v = q.popleft()

                for node in graph[v]:
                    in_degree[node] -= 1
                    index_set[node] = index_set[node] | index_set[v] | set([v])
                    if in_degree[node] == 0:
                        q.append(node)

        print(index_set)
        res = []
        for a, b in queries:
            res.append(a in index_set[b])

        return res

