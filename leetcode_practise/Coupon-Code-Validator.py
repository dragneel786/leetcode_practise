class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        bs_order = {"electronics":1, "grocery":2,\
         "pharmacy":3, "restaurant":4}
        res = []
        for kode, bns, active in zip(code, businessLine, isActive):
            if len(kode):
                for c in kode:
                    if not c.isalnum() and c != '_':
                        break
                else:
                    if bns in bs_order and active:
                        res.append((bs_order[bns], kode))
        
        res.sort()
        return [_ for k, _ in res]


