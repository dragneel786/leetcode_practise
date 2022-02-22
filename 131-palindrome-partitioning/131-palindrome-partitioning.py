class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def getPartition(s, res, op = []):
            if(not s):
                res.append(op)
                return

            for k in range(len(s)):
                if(s[:k + 1] == s[:k + 1][::-1]):
                    getPartition(s[k + 1:], res, op + [s[:k + 1]])
                    
        
        getPartition(s, res)
        return res