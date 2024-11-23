class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        rotated = [([""] * rows) for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                rotated[c][rows - r - 1] = box[r][c]



        for r in range(cols - 1, 0, -1):
            for c in range(rows):
                tr = r
                while(tr < cols):
                    if rotated[tr][c] == '.' and\
                    rotated[tr - 1][c] == '#':
                        rotated[tr][c], rotated[tr - 1][c] = \
                        rotated[tr - 1][c], rotated[tr][c]
                        tr += 1

                    else:
                        break


        return rotated
        