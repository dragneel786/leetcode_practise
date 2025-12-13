class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def is_valid_code(val):
            if len(val) == 0:
                return False
                
            if val.isalnum():
                return True
            
            for c in val:
                if not c.isalnum() and c != '_':
                    return False
                
            return True

        res = []
        line = {"electronics":1, "grocery":2, "pharmacy":3, "restaurant":4}
        for c, b, isA in zip(code, businessLine, isActive):
            if not isA or b not in line or not is_valid_code(c): 
                continue
            
            res.append([line[b], c])
        
        return [c for _, c in sorted(res)]
            

