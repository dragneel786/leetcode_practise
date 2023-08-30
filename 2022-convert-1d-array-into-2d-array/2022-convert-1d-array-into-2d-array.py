class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        if(m * n != len(original)):
            return []
        
        res = []
        for i in range(m):
            col = []
            for j in range(n):
                col.append(original[(i * n) + j])
            
            res.append(col)
        
        return res
        