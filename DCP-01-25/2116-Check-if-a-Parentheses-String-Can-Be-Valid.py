class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
            
        opens = deque()
        unlocked = deque()
        for i, p in enumerate(locked):
            if p == '0':
                unlocked.append(i)
            
            elif s[i] == '(':
                opens.append(i)
            
            else:
                if opens:
                    opens.pop()
                
                elif unlocked:
                    unlocked.pop()
                
                else:
                    return False

        while(opens and unlocked and opens[-1] < unlocked[-1]):
            opens.pop()
            unlocked.pop()
        
        if opens:
            return False
        
        return True