class Solution:
    def climbStairs(self, n: int, cost: List[int]) -> int:
        heap=[(0,0)]
        distance=[float('inf')]*(n+1)
        distance[0]=0
        while(heap):
            c,i=heapq.heappop(heap)
            if(c<=distance[i]):
                for k in range(1,4):
                    x=i+k
                    if(x-1<n):
                        v=cost[x-1]+(x-i)**2
                        if(distance[x]>c+v):
                            heapq.heappush(heap,(c+v,x))
                            distance[x]=c+v
        return distance[n]
                    
                        
        