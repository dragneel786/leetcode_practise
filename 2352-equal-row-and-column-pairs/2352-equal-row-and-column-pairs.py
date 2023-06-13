class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        def create_trie():
            t = dict()
            for row in grid:
                temp = t
                for v in row:
                    temp[v] = temp.get(v, {})
                    temp = temp[v]
                
                temp[-1] = temp.get(-1, 0) + 1
            
            return t
                
        
        def search():
            nonlocal k
            t = trie
            for i in range(n):
                v = grid[i][k]
                if(v not in t):
                    return False
                t = t[v]
            
            return t[-1]
        
        n = len(grid)
        trie = create_trie()
        count = 0
        for k in range(n):
            count += search()
        
        return count