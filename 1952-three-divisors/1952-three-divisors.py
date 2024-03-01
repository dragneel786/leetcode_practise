class Solution:
    def isThree(self, n: int) -> bool:
        divs = 0
        for d in range(1, n + 1):
            divs += (n % d == 0)
        
        return divs == 3