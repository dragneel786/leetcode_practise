class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        
        def swap():
            ans = s
            q = deque(list(s))
            for _ in range(len(s)):
                q.append(q.popleft())
                ans = min(ans, "".join(q))
            
            return ans
        
        return "".join(sorted(s)) if(k > 1) else swap()
        
            
            