class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        carry = (digits[n] + 1) // 10
        digits[n] = (digits[n] + 1) % 10
        n -= 1
        while(n > -1 and carry):
            val = digits[n] + carry
            carry = val // 10
            digits[n] = val % 10
            n -= 1

        if(carry):
            digits = [carry] + digits

        return digits
        