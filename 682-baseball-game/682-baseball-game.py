class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for o in ops:
            if(o == '+'):
                res.append(res[-1] + res[-2])
            elif(o == 'D'):
                res.append(res[-1] * 2)
            elif(o == "C"):
                res.pop()
            else:
                res.append(int(o))
        
        return sum(res)