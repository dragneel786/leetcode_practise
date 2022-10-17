class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        right = deque([i for i, s in enumerate(seats) if(s)])
        ans = 0
        left = -1
        for i, s in enumerate(seats):
            if(right and i == right[0]):
                left = right.popleft()
            else:
                comp = inf
                if(right):
                    comp = min(comp, right[0] - i)
                
                if(left != -1):
                    comp = min(comp, i - left)
                
                ans = max(comp, ans)
        
        return ans
                