# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.q = deque()
    
    def read(self, buf: List[str], n: int) -> int:
        # print(self.q)
        def from_q(buf):
            nonlocal n, chars
            while(n and self.q):
                buf[chars] = self.q.popleft()
                n -= 1
                chars += 1
            
        def to_q(buf):
            for j in range(4):
                if(not buf[j]): 
                    break
                self.q.append(buf[j])
            
            return j
                
        chars = 0
        if(self.q): from_q(buf)
        
        while(n):
            buf4 = [''] * 4
            read4(buf4)
            
            if(to_q(buf4) == 0):
                break
                
            from_q(buf)
            
        return chars
        
        