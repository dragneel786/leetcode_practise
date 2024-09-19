class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = ['+', '-', '*']
        for op in ops:
            if op in expression:
                break
        else:
            return [int(expression)]
        
        res = []
        for i in range(len(expression)):
            if expression[i] in ops:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                
                for l in left:
                    for r in right:
                        res.append(eval(f'{l}{expression[i]}{r}'))
        
        return res
                        
                
                
        
        
        