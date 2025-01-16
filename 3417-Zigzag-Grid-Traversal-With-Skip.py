class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        zig = zag = True
        for row in grid:
            for v in (row if zig else row[::-1]):
                if zag:
                    res.append(v)
                
                zag = not zag
            
            zig = not zig
        
        return res