class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.genPara(res, n, n)
        return res

    def genPara(self, res, closing, opening, op = ""):
        if(closing == 0 and opening == 0):
            res.append(op)
            return

        if(closing < 0 or opening < 0):
            return

        if(opening < closing):
            self.genPara(res, closing, opening - 1, op + "(")
            self.genPara(res, closing - 1, opening, op + ")")
        else:
            self.genPara(res, closing, opening - 1, op + "(")