class Solution:
    def lengthLongestPath(self, input: str) -> int:
        paths = input.split("\n")
        st = deque()
        res = 0
        for p in paths:
            tab = 0
            isFile = False
            for i in range(len(p)):
                if(p[i] == "\t"):
                    tab += 1
                
                if(p[i] == "."):
                    isFile = True
            
            while(st and st[-1][0] >= tab):
                poped = st.pop()
                if(poped[2]):
                    res = max(res, len(poped[1]))
            if(st):
                path = st[-1][1] + "/" + p[tab:]
            else:
                path = p[tab:]
            st.append((tab, path, isFile))
    
        while(st):
            poped = st.pop()
            if(poped[2]):
                res = max(res, len(poped[1]))
        return res
                
                    