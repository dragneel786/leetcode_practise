class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(":")
        ans = [start]
        while(start != end):
            row, col = start[:]
            if(col < end[1]):
                col = str(int(col) + 1)
            else:
                row = chr(ord(row) + 1)
                col = s[1]
            
            start = row + col
            ans.append(start)
    
        return ans