class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        digits[0] += 1
        carry = 0
        
        for i in range(len(digits)):
            val = digits[i] + carry
            digits[i], carry = val % 10, val // 10
            
            if(not carry): return digits[::-1]
        
        if(carry):
            digits.append(carry)
        
        return digits[::-1]
            
            
        