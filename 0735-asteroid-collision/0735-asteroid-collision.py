class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = deque()
        for ast in asteroids:
            if(ast > 0):
                st.append(ast)
                continue
                
            while(st and st[-1] > 0 and \
                  abs(st[-1]) < abs(ast)):
                st.pop()
                
            if(not st):
                st.append(ast)
            
            elif(st[-1] * ast > 0):
                st.append(ast)
            
            elif(abs(st[-1]) == abs(ast)):
                st.pop()
        
        return st