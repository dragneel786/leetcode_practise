class Solution:
    def reverseWords(self, s: str) -> str:
        que = deque()
        i = 0
        n = len(s)
        while(i < n):
            j = i
            while(i < n and s[i] != ' '):
                i += 1
            
            if(i != j): que.appendleft(s[j: i])
            
            i += 1
        
        return ' '.join(que)
        
                
        print(que)