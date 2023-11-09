class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        freq = [g.count(1) for g in grid]
        idx = -1
        cc = -1
        for i, f in enumerate(freq):
            if(f > cc):
                idx = i
                cc = f
        
        return idx
        