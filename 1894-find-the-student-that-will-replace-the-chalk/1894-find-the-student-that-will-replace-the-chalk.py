class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tot = sum(chalk)
        remain = k % tot
        for i, c in enumerate(chalk):
            if remain < c:
                return i
            
            remain -= c 
        
        return -1
        