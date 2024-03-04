class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        start = 0
        end = len(tokens) - 1
        score = max_score = 0
        while(start <= end):
            if(power >= tokens[start]):
                power -= tokens[start]
                score += 1
                start += 1
                
            elif(score > 0):
                power += tokens[end]
                end -= 1
                score -= 1
                
            else:
                break
            
            # print(score)
            max_score = max(score, max_score)
        
        return max_score
            
            
            
            
            