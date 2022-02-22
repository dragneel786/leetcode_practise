class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def getPartition(s, op = []):
            if(not s):
                return [op.copy()]

            res = []
            for k in range(len(s)):
                if(s[:k + 1] == s[:k + 1][::-1]):
                    res.extend(getPartition(s[k + 1:], op + [s[:k + 1]]))

            return res

        return getPartition(s)

