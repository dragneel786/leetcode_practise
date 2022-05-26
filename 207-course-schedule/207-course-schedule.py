class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(lambda:[])
        for p in prerequisites:
            graph[p[0]].append(p[1])

        indeg = [0] * numCourses
        for i in range(numCourses):
            for v in graph[i]:
                indeg[v] += 1

        def addZeroDeg():
            for i in range(numCourses):
                if(not indeg[i] and i not in visited):
                    q.appendleft(i)


        q = deque()
        count = 0
        visited = set()
        addZeroDeg()
        while(len(q)):
            for _ in range(len(q)):
                node = q.pop()
                count += 1
                visited.add(node)
                for v in graph[node]:
                    indeg[v] -= 1
            addZeroDeg()
        return count == numCourses