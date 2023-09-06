class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        idx = 0
        while(idx < len(command)):
            ch = ''
            if(command[idx] == 'G'):
                ch = "G"
                idx += 1
            
            elif(command[idx: idx + 2] == '()'):
                ch = "o"
                idx += 2
            
            else:
                idx += 4
                ch = 'al'
            
            ans.append(ch)
        
        return ''.join(ans)
                