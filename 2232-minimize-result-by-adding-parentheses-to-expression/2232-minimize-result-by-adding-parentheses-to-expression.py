class Solution:
    def minimizeResult(self, expression: str) -> str:
        def prod(val):
            if(not val):
                return 1
        
            return reduce(lambda a, b: a * b, map(int, val.split()))
    
        num1, num2 = expression.split('+')
        minv = inf
        ans = ""
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2)):
                s = int(num1[i:]) + int(num2[:j + 1])
                val = prod(num1[:i]) * s * prod(num2[j + 1:])
                if(minv > val):
                    minv = val
                    ans = f'{num1[:i]}({num1[i:]}+{num2[:j + 1]}){num2[j + 1:]}'
        
        return ans