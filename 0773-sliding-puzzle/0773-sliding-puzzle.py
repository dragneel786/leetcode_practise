class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        def mat_to_str(mat):
            return ''.join([v for m in mat for v in m])
        
        def str_to_mat(mat):
            splits = list(mat)
            mat = [splits[v: v + 3] for v in range(0,6,3)]
            return mat
            
        def gen_states(curr_state):
            gstates = []
            _board = str_to_mat(curr_state)
            zr = zc = 0
            for r in range(2):
                for c in range(3):
                    if _board[r][c] == '0':
                        zr, zc = r, c
                        break
                        
            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr, nc = zr + dr, zc + dc
                if(0 <= nr < 2 and 0 <= nc < 3):
                    _board[nr][nc], _board[zr][zc] = \
                    _board[zr][zc], _board[nr][nc]
                    gstates.append(mat_to_str(_board))
                    _board[nr][nc], _board[zr][zc] = \
                    _board[zr][zc], _board[nr][nc]
            
            return gstates
            
        
        for i in range(len(board)):
            board[i] = list(map(str, board[i]))
          
        final_state = "123450"
        start = mat_to_str(board)
        q = deque([start])
        visited = set([start])
        steps = 0
        while(q):
            for _ in range(len(q)):
                pop_state = q.popleft()
                if pop_state == final_state:
                    return steps
                    
                states = gen_states(pop_state)
                for state in states:
                    if state not in visited:
                        visited.add(state)
                        q.append(state)
                        
            steps += 1
        
        return -1
            
        