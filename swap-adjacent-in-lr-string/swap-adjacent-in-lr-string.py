class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        
        def find_and_swap(pos, char_needed, char_has):
            if(not pos):
                return False
            
            j = pos
            while(j > -1):
                if(char_needed == start[j]):
                    start[j], start[pos] = start[pos], start[j]
                    return True
                
                if(char_has != start[j]):
                    return False
                
                j -= 1
            
            return False
                    
            
        start = list(start)
        end = list(end)
        for i in range(len(start) - 1, -1, -1):
            if(start[i] != end[i]):
                if(start[i] == 'L' and end[i] == 'X'):
                    if(not find_and_swap(i, 'X', start[i])):
                        return False
                
                elif(start[i] == 'X' and end[i] == 'R'):
                    if(not find_and_swap(i, 'R', start[i])):
                        return False
                else:
                    return False
        
        return True
        