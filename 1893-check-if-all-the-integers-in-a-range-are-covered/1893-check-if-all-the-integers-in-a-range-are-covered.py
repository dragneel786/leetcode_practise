class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        cover = [1] * 51
        for s, e in ranges:
            for i in range(s, e + 1):
                cover[i] = 0
        
        for j in range(left, right + 1):
            if(cover[j]):
                return False
        
        return True
                