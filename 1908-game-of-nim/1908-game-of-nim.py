class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        turn_it = lambda name: 'Alice' if(name == 'Bob') else 'Bob'
        
        def winner(paras):
            key = '-'.join(map(str, paras))
            if(key in memo):
                return memo[key]
            
            if(sum(paras) == 0):
                return False
            
            for i in range(len(paras)):
                tp = paras[i]
                for _ in range(paras[i]):
                    paras[i] -= 1
                    if(not winner(sorted(paras))):
                        memo[key] = True
                        return True
                paras[i] = tp
            
            memo[key] = False
            return False
        
        memo = dict()
        return winner(piles)
                
                    