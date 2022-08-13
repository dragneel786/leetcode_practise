class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        combos = {1: ['0', '1', '8']}
        combos[2] = ['11', '69', '88', '96']
        combos[4] = ['00', '11', '69', '88', '96']
        
        def split_add(p1, p2):
            if(not p2 or not p1):
                return p1 if(p1) else p2
            
            temp = []
            for o in p1:
                mid = len(o) // 2
                h1, h2 = o[:mid], o[mid:]
                for c in p2:
                    temp.append(h1 + c + h2)
            
            return temp
        
        def create_number(n, op = []):
            nonlocal res
            if(n <= 1):
                op = split_add(op, combos[1]) if(n == 1) else op
                res = op[:]
                return 
            
            if(n == 2 or n == 3):
                op = split_add(combos[2], op)
                create_number(n - 2, op)
                return
                
            op = split_add(combos[4], op)
            create_number(n - 2, op)
                
        
        res = []
        create_number(n)
        return res
        