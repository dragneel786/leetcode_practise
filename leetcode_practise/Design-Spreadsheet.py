class Spreadsheet:

    def __init__(self, rows: int):
        self.size = rows
        self.cell_hash = dict()

    def setCell(self, cell: str, value: int) -> None:
        self.cell_hash[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.cell_hash:
            del self.cell_hash[cell]

    def getValue(self, formula: str) -> int:
        v1, v2 = formula[1:].split("+")
        val1 = val2 = 0
        if v1.isdigit():
            val1 = int(v1)
        else:
            val1 = int(self.cell_hash.get(v1, 0))
            
        
        if v2.isdigit():
            val2 = int(v2)
        else:
            val2 = int(self.cell_hash.get(v2, 0))
            
        return val1 + val2
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)