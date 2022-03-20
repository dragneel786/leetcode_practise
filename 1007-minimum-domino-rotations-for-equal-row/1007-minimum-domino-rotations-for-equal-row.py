class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        minRot = float('inf')
        start = [tops[0], bottoms[0]]
        for i in range(2):
            topRot = 0
            botRot = 0
            possible = True
            for j in range(len(tops)):
                if(tops[j] == start[i] or bottoms[j] == start[i]):
                    topRot += 1 if(start[i] != tops[j]) else 0
                    botRot += 1 if(start[i] != bottoms[j]) else 0
                else:
                    possible = False
                    break;
                    
            if(possible):
                minRot = min(minRot, min(topRot, botRot))
        
        return -1 if(minRot == float('inf')) else minRot
            