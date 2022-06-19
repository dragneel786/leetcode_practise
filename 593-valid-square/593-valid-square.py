class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(p1, p2):
            if(p1[0] == p2[0] and p1[1] == p2[1]): return False
            sides.add(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
            return True
        
        sides = set()
        return dist(p1, p2) and dist(p1, p3) and dist(p1, p4)\
                and dist(p2, p3) and dist(p2, p4) and dist(p3, p4) and len(sides) == 2
         
         