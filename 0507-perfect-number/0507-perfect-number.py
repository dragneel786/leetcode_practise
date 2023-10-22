class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        div_total = 1
        for div in range(2, int(sqrt(num)) + 1):
            div_total += 0 if(num % div) else (div + num // div)
            
        return num != 1 and div_total == num