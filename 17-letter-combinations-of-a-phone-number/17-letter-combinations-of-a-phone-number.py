class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        if(len(digits) == 0):
            return []
        letters = []
        for i in range(len(digits)):
            letters.append(keypad[int(digits[i])])

        res = []
        self.getCombo(letters, res)
        return res
    
    def getCombo(self, letters, res, op = ""):
        if(not letters):
            res.append(op)
            return

        for i in letters[0]:
            self.getCombo(letters[1:], res, op + i) 