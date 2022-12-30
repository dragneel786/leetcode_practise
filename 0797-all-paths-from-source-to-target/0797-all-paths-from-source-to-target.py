class Solution:
    def allPathsSourceTarget(self, graphi: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        for i, vs in enumerate(graphi):
            for num in vs:
                graph[i].append(num)
                
        que = deque([[0]])
        ans = []
        n = len(graphi)
        while(que):
            for _ in range(len(que)):
                li = que.popleft()
                if(li[-1] == n - 1):
                    ans.append(li)
                    continue
                
                for v in graph[li[-1]]:
                    que.append(li + [v])
        
        return ans
        
                
        