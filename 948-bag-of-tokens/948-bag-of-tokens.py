class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        down = len(tokens) - 1
        score = up = 0
        
        while(up <= down):
            if(power >= tokens[up]):
                score += 1
                power -= tokens[up]
                up += 1
            
            elif(score >= 1 and up != down):
                power += tokens[down]
                score -= 1
                down -= 1
            
            else:
                break
        
        return score
                
                
        