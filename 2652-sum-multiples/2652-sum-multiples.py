class Solution:
    def sumOfMultiples(self, n: int) -> int:
        tot = 0
        for num in range(1, n + 1):
            if(num % 3 == 0):
                tot += num
            
            elif(num % 5 == 0):
                tot += num
            
            elif(num % 7 == 0):
                tot += num
        
        return tot