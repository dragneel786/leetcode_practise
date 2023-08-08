class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        
        def calculate(scores):
            start = -3
            res = 0
            for i, s in enumerate(scores):
                adder = s
                if(i - start <= 2):
                    adder *= 2
                res += adder
                
                if(s == 10):
                    start = i
            
            return res
        
        v1 = calculate(player1)
        v2 = calculate(player2)
        return 0 if(v1 == v2) else 1 if(v1 > v2) else 2
                
                
                    