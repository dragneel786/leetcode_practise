class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if(k >= n):
            return max(arr)
        
        q = deque(arr)
        for i in range(n):
            ele = q.popleft()
            curr_max = 1 if(i > 0) else 0
            while(ele > q[0] and curr_max < k):
                curr_max += 1
                e = q.popleft()
                q.append(e)
            
            q.append(ele)
            if(curr_max >= k):
                return ele
            
        return ele
        
        