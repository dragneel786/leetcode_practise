class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        st = deque()
        m = len(board)
        n = len(board[0])
        for row in range(m):
            for col in range(n):
                neigh = 0
                for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0],\
                             [1, 1], [-1, 1], [1, -1], [-1, -1]]:
                    r = row + i
                    c = col - j
                    if(r < 0 or c < 0 or r >= m or c >= n or not board[r][c]):
                        continue
                    neigh += 1
                
                if(not board[row][col] and neigh == 3):
                    st.append([row, col, 1])
                elif(board[row][col] and (neigh < 2 or neigh > 3)):
                    st.append([row, col, 0])
                
        while(len(st)):
            row, col, val = st.pop()
            board[row][col] = val
        