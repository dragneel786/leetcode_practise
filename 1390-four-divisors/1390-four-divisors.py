class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def get_divs(val):
            d = []
            s = 1
            while((s * s) <= val):
                if val % s == 0:
                    d.append(s)
                    div = val // s
                    if div != s:
                        d.append(div)
                
                s += 1
            
            return d
        
        tot = 0
        for num in nums:
            divs = get_divs(num)
            if len(divs) == 4:
                tot += sum(divs)
            
        return tot