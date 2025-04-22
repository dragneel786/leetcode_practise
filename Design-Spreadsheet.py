class Spreadsheet:

    def __init__(self, rows: int):
        self.spread_sheet = Counter()

    def setCell(self, cell: str, value: int) -> None:
        self.spread_sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        del self.spread_sheet[cell]

    def getValue(self, formula: str) -> int:
        c1, c2 = formula[1:].split('+')
        v1 = v2 = 0
        if c1.isdigit():
            v1 = int(c1)
        else:
            v1 = self.spread_sheet[c1]
        
        if c2.isdigit():
            v2 = int(c2)
        else:
            v2 = self.spread_sheet[c2]
        
        return v1 + v2


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)