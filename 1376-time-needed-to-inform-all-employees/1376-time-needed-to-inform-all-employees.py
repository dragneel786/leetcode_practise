class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        mang = defaultdict(lambda:[])
        for i in range(n):
            mang[manager[i]].append(i)

        st = deque()
        st.append([headID, 0])
        maxV = float('-inf')
        while(len(st)):
            for _ in range(len(st)):
                m = st.pop()
                t = informTime[m[0]]
                if(not t):
                    maxV = max(maxV, m[1])
                    continue

                for c in mang[m[0]]:
                    st.appendleft([c, m[1] + t])

        return maxV
                        
        