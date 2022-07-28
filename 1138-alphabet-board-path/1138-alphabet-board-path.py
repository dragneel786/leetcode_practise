class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        
        def createBoard():
            alpha = dict()
            for r, row in enumerate(["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]):
                for c, ch in enumerate(row):
                    alpha[ch] = (r, c)
            return alpha
        
        def bfs(start, end):
            dic = {"U":(-1, 0), "D": (1, 0), "R":(0, 1), "L":(0, -1)}
            q = deque([(start, "")])
            visited = set([start])
            while(q):
                (x, y), steps = q.popleft()
                if((x, y) == end):
                    return steps + "!"
                
                for di, (dx, dy) in dic.items():
                    nx, ny = x + dx, y + dy
                    if((nx, ny) not in visited and\
                       (nx, ny) in validPositions):
                        q.append(((nx, ny), steps + di))
                        visited.add((nx, ny))
            
        board = createBoard()
        validPositions = set(board.values())
        prev = "a"
        res = ""
        for curr in target:
            res += bfs(board[prev], board[curr])
            prev = curr
        return res
                