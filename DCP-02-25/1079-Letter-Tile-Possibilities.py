class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        def possible(s, visited):
            if len(visited) == len(tiles):
                vset.add(s)
                return
            
            for i in range(len(tiles)):
                if i not in visited:
                    visited.add(i)
                    possible(s, visited)
                    possible(s + tiles[i], visited)
                    visited.remove(i)
            
        vset = set()
        possible("", set())
        return len(vset) - 1
        