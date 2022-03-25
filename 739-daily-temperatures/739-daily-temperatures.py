class Solution:
    def dailyTemperatures(self, tempt: List[int]) -> List[int]:
        st = deque()
        res = [0] * len(tempt)
        for i in range(len(tempt)):
            while(len(st) and tempt[i] > tempt[st[-1]]):
                idx = st.pop()
                res[idx] = i - idx
            
            st.append(i)
        
        return res
                
                