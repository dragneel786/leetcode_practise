class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # 0 0 1 0 1 1
        #   3 2 2 1 0
        #   8 5 3 1 0
        # 2 + 4 + 5
        n = len(boxes)
        lefts = [0] * n
        rights = [0] * n
        currL = currR = 0
        for i in range(n):
            bi = n - i - 1
            if i > 0:
                lefts[i] = lefts[i - 1] + currL

            if bi < n - 1:
                rights[bi] = rights[bi + 1] + currR
            
            currL += boxes[i] == '1'
            currR += boxes[bi] == '1'
        
        res = []
        for a, b in zip(lefts, rights):
            res.append(a + b)
        
        return res
        

            