class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if(len(s) != len(goal)):
            return False
        
        if(s == goal):
            return len(s) > 26 or\
        len(set(s)) != len(s)
        
        diff = dict()
        for a, b in zip(s, goal):
            if(a != b):
                if(a in diff or len(diff) >= 2):
                    return False
                
                diff[a] = b
                
        return sorted(diff.keys()) == sorted(diff.values())
    