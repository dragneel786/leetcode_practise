class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], clen: int) -> int:
        tiles.sort()
        res = cover = 0
        i = j = 0
        while(res < clen and i < len(tiles)):
            if(tiles[j][0] + clen > tiles[i][1]):
                cover += tiles[i][1] - tiles[i][0] + 1
                res = max(cover, res)
                i += 1
            else:
                partial = max(0, tiles[j][0] + clen - tiles[i][0])
                res = max(res, cover + partial)
                cover -= (tiles[j][1] - tiles[j][0] + 1)
                j += 1
        return res
                
                
                
            