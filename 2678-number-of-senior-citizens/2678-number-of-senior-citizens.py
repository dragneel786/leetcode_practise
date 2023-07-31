class Solution:
    def countSeniors(self, details: List[str]) -> int:
        pattern = r'[MFO]'
        counts = 0
        for detail in details:
            counts += int(re.split(pattern, detail)[1][:2]) > 60
        
        return counts