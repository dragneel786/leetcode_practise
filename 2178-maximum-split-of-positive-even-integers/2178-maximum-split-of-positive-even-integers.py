class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if(finalSum & 1):
            return []
        
        res = set()
        for n in range(2, finalSum, 2):
            val1, val2 = n, finalSum - n
            if(val1 == val2 or val1 in res or val2 in res or not finalSum):
                break
            res.add(n)
            finalSum -= n
            
        if(finalSum):
            res.add(finalSum)
        return res
        