class Solution:
    def numberToWords(self, num: int) -> str:
        
        def helper_of_helper(val):
            ones_map = ["Eleven", "Twelve", "Thirteen", "Fourteen",\
                        "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            if 10 < val < 20:
                return ones_map[val - 11]
            
            return None
            
        
        def helper(val):
            single = ["One", "Two", "Three", "Four", \
                      "Five", "Six", "Seven", "Eight", "Nine"]
            double = ["Ten", "Twenty", "Thirty", "Forty",\
                      "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
            ret = []
            divs = 100
            while(val):
                hh = helper_of_helper(val)
                if hh is not None:
                    ret.append(hh)
                    break 
                
                mod = val // divs
                if mod > 0:
                    if divs == 1:
                        ret.append(single[mod - 1])
                    
                    elif divs == 10:
                        ret.append(double[mod - 1])
                    
                    else:
                        ret.append(single[mod - 1])
                        ret.append("Hundred")
                        
                val %= divs
                divs //= 10
            # print(val)  
            return ret
        
        if num == 0:
            return "Zero"
        
        mills = ["Billion", "Million", "Thousand"]
        divi = 1_000_000_000
        itr = 0
        res = []
        while(num):
            temp = helper(num // divi)
            if temp:
                res.extend(temp)
                if itr < len(mills):
                    res.append(mills[itr])
            
            # print(temp, mills[itr])
            num %= divi
            divi //= 1000
            itr += 1
            
        
        return ' '.join(res)
            
                        
                        
                    