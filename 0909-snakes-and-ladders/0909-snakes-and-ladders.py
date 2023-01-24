class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        def create_bmap():
            dire = True
            bmap = {}
            counter = 1
            for r in range(n - 1, -1, -1):
                col = None
                for c in range(n):
                    if(dire):
                        col = c
                    else:
                        col = n - c - 1

                    bmap[counter] = board[r][col]
                    counter += 1
                dire = not dire
            
            return bmap
        
        
        n = len(board)
        dest = n ** 2
        bmap = create_bmap()
        q = deque([(1, False)])
        visited = set([(1, False)])
        steps = 0
        while(q):
            for _ in range(len(q)):
                pos, neutral = q.popleft()
                if(pos == dest):
                    return steps
                
                for new_pos in range(min(pos + 6, dest), pos, -1):
                    state = None
                    if(bmap[new_pos] == -1):
                        state = (new_pos, False)
                    elif(bmap[new_pos] and not neutral):
                        state = (bmap[new_pos], False)
                    else:
                        state = (new_pos, False)
                    
                    if(state not in visited):
                        visited.add(state)
                        q.append(state)
                        
            
            steps += 1
        
        return -1
        
                
                