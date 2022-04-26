class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [True] + [False for _ in range(n - 1)]
        disArr = [0] + [math.inf for _ in range(n - 1)]
        tot = 0
        edges = 0
        curr = 0
        while(edges < n - 1):
            minE = math.inf
            nextP = 0
            for i in range(n):
                if(not visited[i]):
                    dis = abs(points[curr][0] - points[i][0])\
                    + abs(points[curr][1] - points[i][1])
                    disArr[i] = min(dis, disArr[i])
                    
                    if(minE > disArr[i]):
                        minE = disArr[i]
                        nextP = i
                    
            edges += 1
            curr = nextP
            tot += minE
            visited[curr] = True
        
        return tot
                