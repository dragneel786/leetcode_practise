class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def words_trie(words):
            trie = dict()
            for word in words:
                t = trie
                for c in word:
                    t[c] = t.get(c, {})
                    t = t[c]
                
                t['$'] = word
        
            return trie
        
        
        def dfs(x, y, triee, visited):
            if('$' in triee):
                res.append(triee['$'])
                del triee['$']
            
            visited.add((x, y))
            for dx, dy in [(0, 1), (1, 0),
                           (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if(0 <= nx < rows and 0 <= ny < cols\
                   and (nx, ny) not in visited and\
                   triee.get(board[nx][ny], None)):
                    
                    dfs(nx, ny, triee[board[nx][ny]], visited)
                    if(not triee[board[nx][ny]]):
                        del triee[board[nx][ny]]
            
            visited.remove((x, y))
                    
        
        trie = words_trie(words)
        rows, cols = len(board), len(board[0])
        res = []
        
        for r in range(rows):
            for c in range(cols):
                if(board[r][c] in trie):
                    dfs(r, c, trie[board[r][c]], set())
        
        return res
        
        
            