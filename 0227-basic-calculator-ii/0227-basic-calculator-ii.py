class Solution:
    def calculate(self, s: str) -> int:
        def perform(a, op, b):
            if(op == '+'):
                res = int(a) + int(b)
            
            if(op == "-"):
                res = int(a) - int(b)
            
            if(op == '*'):
                res = int(a) * int(b)
            
            if(op == '/'):
                res = int(a) // int(b)
            
            return str(res)
        
        def get_num(i, st):
            num = ''
            while(i < len(st) and st[i].isdigit()):
                num += st[i]
                i += 1
            
            return num, i
            
        def calcu(st, ops):
            prev_num, i = get_num(0, st)
            op = ""
            new_s = []
            while(True):
                if(i == len(st)):
                    break
                op = st[i]
                next_num, i = get_num(i + 1, st)
                
                if(op in ops):
                    prev_num = perform(prev_num, op, next_num)
                
                else:
                    new_s.append(prev_num)
                    new_s.append(op)
                    prev_num = next_num
                    
            return new_s + [prev_num]
        
        s = s.replace(" ", "")
        if(all([c.isdigit() for c in s])):
            return int(s)
        first = calcu(s, ['*', '/'])
        if(len(first) > 1):
            second = calcu(''.join(first), ['+', '-'])
        else:
            second = first
        return int(second[0])
        
        
        
            
            
            