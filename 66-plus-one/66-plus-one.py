class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        rem = 1
        for i in range(len(digits) - 1, -1, -1):
            if(rem == 0):
                return digits[1:]

            sumVal = (digits[i] + rem)
            digits[i] = sumVal % 10
            rem = sumVal // 10

        return digits