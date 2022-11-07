class Solution:
    def maximum69Number (self, num: int) -> int:
        idx = -1
        place = 1
        temp = num
        while(temp):
            last = temp % 10
            temp //= 10
            
            if(last == 6):
                idx = place
                
            place += 1
        
        if(idx == -1): return num
        
        popi = (10 ** idx)
        return (num // popi * popi + (9 * popi // 10) + (num % (popi //10)))
            