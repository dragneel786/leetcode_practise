class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        ret = []
        for i, c in enumerate(expression):
            if(not c.isdigit()):
                part1 = self.diffWaysToCompute(expression[:i])
                part2 = self.diffWaysToCompute(expression[i + 1:])
                
                for p1 in part1:
                    for p2 in part2:
                        ret.append(eval(str(p1) + c + str(p2)))
        
        if(not ret):
            ret.append(int(expression))
            
        return ret
                    
            