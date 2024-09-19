class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        ops = ['+','-','*']
        for i in range(len(expression)):
            if expression[i] in ops:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                
                for l in left:
                    for r in right:
                        res.append(eval(f'{l}{expression[i]}{r}'))
        
        return res if res else [int(expression)]
                        
                
                
        
        
        