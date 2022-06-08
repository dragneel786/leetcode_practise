class Solution:
    def racecar(self, target: int) -> int:
        st = deque([(0, 0, 1)])
        visited = set()
        
        while(st):
            moves, position, speed = st.popleft()
            
            if(position == target):
                return moves
            
            if((position, speed) in visited):
                continue
            
            visited.add((position, speed))
            st.append((moves + 1, position + speed, speed * 2))
            
            if((position * speed > target and speed > 0) or\
               ((position * speed) < target and speed < 0)):
                speed = 1 if(speed < 0) else -1
                st.append((moves + 1, position, speed))