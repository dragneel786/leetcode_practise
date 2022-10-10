class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def create_word_trie(words):
            tries = dict()
            for word in words:
                temp = tries
                for c in word:
                    temp[c] = temp.get(c, dict())
                    temp = temp[c]
                temp['$'] = word
                
            return tries
        
        
        def dfs(x, y, t):
            letter = board[x][y]
            node = t[letter]
            
            val = node.pop('$', False)
            if(val):
                ans.append(val)
            
            board[x][y] = None
                
            for dx, dy in [(1, 0), (0, 1),\
                           (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                
                if(0 <= nx < m and 0 <= ny < n\
                   and board[nx][ny] in node):
                    dfs(nx, ny, node)
                    
            board[x][y] = letter
            
            if(not node):
                t.pop(letter)  
        
        
        trie = create_word_trie(words)
        m, n = len(board), len(board[0])
        ans = []
        for r in range(m):
            for c in range(n):
                if(board[r][c] in trie):
                    dfs(r, c, trie)
        
        return ans
                    
        