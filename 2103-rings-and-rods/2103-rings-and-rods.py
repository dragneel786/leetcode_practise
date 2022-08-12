class Solution:
    def countPoints(self, rings: str) -> int:
        rods = defaultdict(set)
        for i in range(0, len(rings), 2):
            color, rod = rings[i], int(rings[i + 1])
            rods[rod].add(color)
        
        counts = 0
        for i in range(10):
            if(len(rods[i]) >= 3):
                counts += 1
        
        return counts
        
        
        
        
        
            