class Solution:
    def maxDepth(self, s: str) -> int:
        ans = opara = 0
        for c in s:
            if(c == "("):
                opara += 1
            elif(c == ")"):
                ans = max(ans, opara)
                opara -= 1
        
        return ans