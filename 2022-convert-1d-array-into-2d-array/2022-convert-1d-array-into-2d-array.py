class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if (m * n) != len(original):
            return []
        
        res = []
        curr = []
        for i, v in enumerate(original):
            curr.append(v)
            if (i + 1) % n == 0:
                res.append(curr)
                curr = []
        
        return res
                
        