class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = 0
        for s in strs:
            val = 0
            for c in s:
                if(not c.isdigit()):
                    val = len(s)
                    break
            else:
                val = int(s)
        
            res = max(res, val)
        return res