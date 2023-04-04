class Solution:
    def partitionString(self, s: str) -> int:
        chars = set()
        count = 1
        for c in s:
            if(c in chars):
                chars = set()
                count += 1
            
            chars.add(c)
    
        return count
            