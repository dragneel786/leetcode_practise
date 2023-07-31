class Solution:
    def countSeniors(self, details: List[str]) -> int:
        pattern = r'[MFO]'
        counts = 0
        for detail in details:
            splits = re.split(pattern, detail)
            counts += int(splits[1][:2]) > 60
        
        return counts