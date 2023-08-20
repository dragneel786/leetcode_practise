class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num = str(num)
        return num == '0' or num == str(num).rstrip('0')