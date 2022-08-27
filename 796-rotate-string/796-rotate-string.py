class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        def compare(pos):
            for c1, c2 in zip(s, goal[i:] + goal[:i]):
                if(c1 != c2):
                    return False
            return True
        
        m, n = len(s), len(goal)
        if(m != n):
            return False
        
        for i, c in enumerate(goal):
            if(c == s[0] and compare(i)):
                return True
        return False