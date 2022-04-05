class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bucks = defaultdict(lambda:0)
        for b in bills:
            if(b == 10):
                if(not bucks[5]):
                    return False
                bucks[5] -= 1
            
            elif(b == 20):
                if(bucks[10] and bucks[5]):
                    bucks[5] -= 1
                    bucks[10] -= 1
                
                elif(bucks[5] >= 3):
                    bucks[5] -= 3
                
                else:
                    return False
            
            bucks[b] += 1
        
        return True
            