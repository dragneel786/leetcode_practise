class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        def check(gidx):
            nonlocal goal, s
            for ch in s:
                if ch != goal[gidx]:
                    return False
            
                gidx = (gidx + 1) % len(goal)
            
            return True
        
        if len(s) == len(goal):
            for i, c in enumerate(goal):
                if c == s[0] and check(i):
                    return True

        return False