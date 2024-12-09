class Solution:
    def canAliceWin(self, n: int) -> bool:
        alice = False
        steps = 10
        while(n >= steps):
            n -= steps
            alice = not alice
            steps -= 1
        
        return alice