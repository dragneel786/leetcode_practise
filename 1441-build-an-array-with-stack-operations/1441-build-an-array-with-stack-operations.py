class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        pu, po = "Push", "Pop"
        res = []
        i = 1
        idx = 0
        while(idx < len(target)):
            if(i == target[idx]):
                res.append(pu)
                idx += 1
            else:
                res.append(pu)
                res.append(po)
            
            i += 1
        
        return res
        