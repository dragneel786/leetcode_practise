class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        sums = 0
        pros = 1
        while(temp):
            sums += temp % 10
            pros *= temp % 10
            temp //= 10
        
        print(sums, pros)
        return (n % (sums + pros)) == 0
        