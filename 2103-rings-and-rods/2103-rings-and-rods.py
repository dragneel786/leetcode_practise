class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [0] * 10
        c_map = {'R':1, 'G':2, 'B':4}
        for color, rod in zip(rings[::2], rings[1::2]):
            rods[int(rod)] |= c_map[color]
        
        return sum(1 for r in rods if(r == 7))
        
        
        
        
        
            