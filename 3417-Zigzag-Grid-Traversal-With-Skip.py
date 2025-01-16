class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        zig = zag = True
        for row in grid:
            rrange = range(len(row)) \
            if zig else range(len(row) - 1, -1, -1)
            
            for i in rrange:
                if zag: res.append(row[i])
                zag = not zag
            
            zig = not zig
        
        return res