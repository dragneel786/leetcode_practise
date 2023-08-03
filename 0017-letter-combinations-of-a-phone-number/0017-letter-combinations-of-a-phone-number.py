class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(len(digits) == 0):
            return []
        
        maps = ["abc", "def", "ghi", "jkl", "mno",\
                "pqrs", "tuv", "wxyz"]
        
        ret = self.letterCombinations(digits[1:])
        res = []
        for c in maps[int(digits[0]) - 2]:
            for r in (ret if(ret) else [""]):
                res.append(c + r)
        
        return res
            