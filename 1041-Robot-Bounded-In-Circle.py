class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        start = sr = sc = 0
        dirs_map = [(0,1), (1,0), (0,-1), (-1,0)]
        for c in instructions:
            if c == 'L':
                start -= 1
                if start < 0:
                    start = 3

            elif c == 'R':
                start = (start + 1) % 4

            else:
                sr, sc = sr + dirs_map[start][0], sc + dirs_map[start][1]

        return start != 0 or (sr, sc) == (0, 0)