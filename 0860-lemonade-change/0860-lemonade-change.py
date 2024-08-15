class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = Counter()
        for b in bills:
            if b == 10:
                if change[5] < 1:
                    return False
                
                change[10] += 1
                change[5] -= 1
            
            elif b == 20:
                if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                
                elif change[5] > 2:
                    change[5] -= 3
                
                else:
                    return False
            
            else:
                change[5] += 1
        
        return True