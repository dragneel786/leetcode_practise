class Solution:
    def partitionString(self, s: str) -> List[str]:
        ret = []
        hset = set()
        curr_run = ""
        for c in s:
            curr_run += c
            if curr_run not in hset:
                hset.add(curr_run)
                ret.append(curr_run)
                curr_run = ""
        
        return ret

            

