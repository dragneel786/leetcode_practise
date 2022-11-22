class Solution:
    def numSquares(self, n: int) -> int:
        dp = {i * i for i in range(1, floor(sqrt(10004)))}
        
        que = deque([(n, 0)])
        res = inf
        while(que):
            num, req = que.popleft()
            if(num in dp):
                return req + 1
            
            for s in range(floor(sqrt(num)), 0, -1):
                val = num - (s ** 2)
                que.append((val, req + 1))
        
        return res
                
            
            
        