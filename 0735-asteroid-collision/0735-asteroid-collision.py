class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = deque()
        for ast in asteroids:
            if(not st):
                st.append(ast)
                
            elif(st[-1] * ast > 0):
                st.append(ast)
                
            else:
                same = False
                while(st and st[-1] > 0 and ast < 0):
                    if(abs(st[-1]) < abs(ast)):
                        st.pop()
                    
                    else:
                        if(abs(st[-1]) == abs(ast)):
                            st.pop()
                            same = True
                        break
            
                if(not same and not st):
                    st.append(ast)
                
                elif(not same and st and st[-1] < 0):
                    st.append(ast)
        
        return st