class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_map = {"L":(0, -1), "R":(0, 1),\
                    "U":(-1, 0), "D":(1, 0)}
        
        pos = [0, 0]
        for move in moves:
            dx, dy = move_map[move]
            pos[0] += dx
            pos[1] += dy
        
        return [0, 0] == pos
            