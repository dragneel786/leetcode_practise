class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        match = j = 0
        for i in range(len(players)):
            while(j < len(trainers) and\
                  players[i] > trainers[j]):
                j += 1
                
            if(j >= len(trainers)):
                break
            
            match += 1
            j += 1
        
        return match
        
        