class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        def getTree():
            g = defaultdict(lambda:[])
            for a,b in edges:
                g[a].append(b)
                g[b].append(a)
            return g
        
        def findClosest(v, nodes):
            visited = set([v])
            q = deque([v])
            while(q):
                for _ in range(len(q)):
                    v = q.popleft()
                    if(v in nodes):
                        return v
                    for ne in tree[v]:
                        if(ne not in visited):
                            q.append(ne)
                            visited.add(ne)
        
        def getPath(start, end, visited):
            if(start == end):
                return [end]
            
            if(start in visited):
                return []
            
            visited.add(start)
            for node in tree[start]:
                temp = getPath(node, end, visited)
                if(temp):
                    temp.append(start)
                    return temp
            return []
            
        tree = getTree()
        ans = []
        for q in query:
            s, e, v = q
            paths = set(getPath(s, e, set()))
            ans.append(findClosest(v, paths))
        return ans
                