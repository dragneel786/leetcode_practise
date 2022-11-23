class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        
        lines = 1
        curr = 0
        for c in s:
            idx = ord(c) - 97
            if(curr + widths[idx] > 100):
                lines += 1
                curr = 0
                
            curr += widths[idx]
        
        return [lines, curr]