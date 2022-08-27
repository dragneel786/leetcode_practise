class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        m, n = len(s), len(goal)
        if(m != n):
            return False
        
        for i, c in enumerate(goal):
            if(c == s[0] and s == goal[i:] + goal[:i]):
                return True
        return False