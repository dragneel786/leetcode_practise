class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        
        dis = lambda x, y: abs(rCenter - x) + abs(cCenter - y)
        return sorted(product(range(rows), range(cols)), key = lambda x: dis(*x))
        