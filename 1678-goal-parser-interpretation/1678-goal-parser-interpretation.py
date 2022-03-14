class Solution:
    def interpret(self, command: str) -> str:
        hash = {"G":"G", "()":"o", "(al)":"al"}
        val = ""
        ans = ""
        for c in command:
            val += c
            if(val in hash):
                ans += hash[val]
                val = ""
            
        return ans