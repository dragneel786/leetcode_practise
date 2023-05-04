class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        banned = [False] * n
        rcount = senate.count('R')
        dcount = n - rcount
        
        def ban(to_ban, start_at):
            pointer = start_at
            while True:
                if(senate[pointer] == to_ban\
                   and not banned[pointer]):
                    banned[pointer] = True
                    break
                
                pointer = (pointer + 1) % n
        
        turn = 0
        while rcount > 0 and dcount > 0:
            if not banned[turn]:
                if senate[turn] == 'R':
                    ban('D', (turn + 1) % n)
                    dcount -= 1
                else:
                    ban('R', (turn + 1) % n)
                    rcount -= 1
                
            turn = (turn + 1) % n
            
        return 'Radiant' if rcount else 'Dire'
                
                    
            
                
                
            