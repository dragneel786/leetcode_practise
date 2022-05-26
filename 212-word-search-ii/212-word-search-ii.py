class Trie:
    def __init__(self):
        self.nodes = defaultdict(lambda:None)
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        head = Trie()
        for w in words:
            self.insertTrie(head, w)
        
        def dfs(r, c, trie):
            if(r < 0 or r >= rows or c < 0 or c >= cols or not board[r][c]):
                return
            
            if(not trie or not trie.nodes[board[r][c]]):
                return
            
            if(trie.nodes[board[r][c]].word):
                ans.add(trie.nodes[board[r][c]].word)
            
            ch = board[r][c]
            board[r][c] = None
            dfs(r - 1, c, trie.nodes[ch])
            dfs(r + 1, c, trie.nodes[ch])
            dfs(r, c - 1, trie.nodes[ch])
            dfs(r, c + 1, trie.nodes[ch])
            board[r][c] = ch
        
        ans = set()
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, head)
        return list(ans)
          
    def insertTrie(self, head, word):
        for w in word:
            if(not head.nodes[w]):
                head.nodes[w] = Trie()
            head = head.nodes[w]
        head.word = word
        