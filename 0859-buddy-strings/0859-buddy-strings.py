class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if(len(s) != len(goal)):
            return False
        
        diff = dict()
        counts = Counter()
        consider = False
        for a, b in zip(s, goal):
            if(a != b):
                if(a in diff or len(diff) >= 2):
                    return False
                
                diff[a] = b
            
            else:
                counts[a] += 1
                if(counts[a] >= 2):
                    consider = True
            
        if(s == goal):
            return consider
         
        return sorted(diff.keys()) == sorted(diff.values())
    