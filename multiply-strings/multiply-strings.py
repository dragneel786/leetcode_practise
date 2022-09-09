class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def create_combo(num1, num2):
            combos = list(itertools.product(num1, num2))
            combos.reverse()
            return [combos[i: i + n] for i in range(
                0, len(combos), n)]
        
        
        def value_carry(val, car):
            return (val + car) % 10, (val + car) // 10
        
        
        def add(res, temp, start):
            c = 0
            for i, v in enumerate(temp, start):
                if(i == len(res)):
                    v, c = value_carry(v, c)
                    res.append(v)
                else:
                    res[i], c = value_carry(res[i] + v, c)
                    
            if(c): res.append(c)
            
        
        if(len(num1) == 1 and int(num1) == 0 or\
          len(num2) == 1 and int(num2) == 0): return '0'
        
        if(len(num1) > len(num2)):
            return self.multiply(num2, num1)
        
        start = 0
        n = max(len(num1), len(num2))
        
        res = []
        combos = create_combo(num1, num2)
        
        for combo in combos:
            temp = []
            carry = 0
            
            for a, b in combo:
                mul, carry = value_carry(int(a) * int(b), carry)
                temp.append(mul)
            
            if(carry): temp.append(carry)
            
            add(res, temp, start)
            print(temp, res)
            start += 1
        
        return ''.join(list(map(str, res)))[::-1]
                
                
                
                
                
        
        
            