class Solution:
    def convertDateToBinary(self, date: str) -> str:
        splits = date.split('-')
        res = []
        for s in splits:
            res.append(bin(int(s))[2:])
        
        return '-'.join(res)
        