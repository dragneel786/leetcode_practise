class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        
        dis = lambda x, y: abs(rCenter - x) + abs(cCenter - y)
        return [coor for coor in sorted([[x, y] for x in range(rows) for y in range(cols)], key = lambda x: dis(*x))]
        