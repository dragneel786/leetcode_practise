class Solution:
    # Direction map for zero's possible moves in a flattened 1D array (2x3 board)
    directions = [
        [1, 3],
        [0, 2, 4],
        [1, 5],
        [0, 4],
        [3, 5, 1],
        [4, 2],
    ]

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Helper method to swap characters at indices i and j in the string
        def _swap(s, i, j):
            s = list(s)
            s[i], s[j] = s[j], s[i]
            return "".join(s)

        # Convert the 2D board into a string representation to use as state
        start_state = "".join(str(num) for row in board for num in row)

        # Dictionary to store the minimum moves for each visited state
        visited = {}

        def _dfs(state, zero_pos, moves):
            # Skip if this state has been visited with fewer or equal moves
            if state in visited and visited[state] <= moves:
                return
            visited[state] = moves

            # Try moving zero to each possible adjacent position
            for next_pos in self.directions[zero_pos]:
                new_state = _swap(
                    state, zero_pos, next_pos
                )  # Swap to generate new state
                _dfs(
                    new_state, next_pos, moves + 1
                )  # Recursive DFS with updated state and move count

        # Start DFS traversal from initial board state
        _dfs(start_state, start_state.index("0"), 0)

        # Return the minimum moves required to reach the target state, or -1 if unreachable
        return visited.get("123450", -1)
#         def mat_to_str(mat):
#             return ''.join([v for m in mat for v in m])
        
#         def str_to_mat(mat):
#             splits = list(mat)
#             mat = [splits[v: v + 3] for v in range(0,6,3)]
#             return mat
            
#         def gen_states(curr_state):
#             _board = str_to_mat(curr_state)
#             zr = zc = 0
#             for r in range(3):
#                 for c in range(3):
#                     if _board[r][c] == '0':
#                         zr, zc = r, c
#                         break
                
#             for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
#                 nr, nc = dr, dc
#                 if(0 <= nr < 3 and 0 <= nc < 3):
#                     _board[nr][nc]
            
        
#         for i in range(len(board)):
#             board[i] = list(map(str, board[i]))
          
#         final_state = "123450"
#         start = mat_to_str(board)
#         q = deque([start])
#         visited = set(start)
#         steps = 0
#         while(q):
#             for _ in range(len(q)):
#                 pop_state = q.popleft()
#                 if pop_state == final_state:
#                     return steps
                    
#                 states = gen_states(pop_state)
#                 for state in states:
#                     if state not in visited:
#                         visited.add(state)
#                         q.append(state)
                        
#             steps += 1
        
        # return -1
            
        