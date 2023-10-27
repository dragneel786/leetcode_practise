class Solution:
    def reformatNumber(self, number: str) -> str:
        n = len(number)
        form = []
        curr = []
        for i, c in enumerate(number + '-'):
            if(c.isdigit()):
                curr.append(c)
            
            if(len(curr) > 4):
                form.append(curr[:3])
                curr = curr[3:]
        
        if(len(curr) == 4):
            form.append(curr[:2])
            form.append(curr[2:])
        else:
            form.append(curr)
        
        return '-'.join(map(lambda x: ''.join(x), form))
                
                