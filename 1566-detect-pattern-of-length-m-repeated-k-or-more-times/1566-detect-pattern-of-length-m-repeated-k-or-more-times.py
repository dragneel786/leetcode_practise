class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        q = deque([(i, i + m, 1) for i in range(n - m)])
        while(q):
            for _ in range(len(q)):
                s, e, count = q.popleft()
                if(count >= k):
                    return True
                
                if(e + m <= n and arr[s: e] == arr[e: e + m]):
                    q.append((s + m, e + m, count + 1))
            
        return False