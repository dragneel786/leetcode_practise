class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        string1 = self.getEditedString(s, n1)
        string2 = self.getEditedString(t, n2)
        if(string1 == string2):
            return True
        return False
    
    def getEditedString(self, s, n):
        back = 0
        temp = ""
        for i in range(n - 1, -1, -1):
            if(s[i] == "#"):
                back += 1
            else:
                if(not back):
                    temp += s[i]
                else:
                    back -= 1
        # print(temp)
        return temp