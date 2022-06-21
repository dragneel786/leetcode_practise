class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: [x[0], -x[1]])
        n = len(properties)
        # st = deque([properties[n - 1]])
        counts = 0
        maxi = 0
        for i in range(n - 1, -1, -1):
            p = properties[i]
            if(p[1] < maxi):
                counts += 1
            maxi = max(maxi, p[1])
            
            # for s in st:
            #     if(s[0] > p[0] and s[1] > p[1]):
            #         counts += 1
            #         break
            # while(not st and st[-1][0] == p[0] and st[-1][1] <= p[1]):
            #     st.pop()
            # if(not st or st[-1][1] < p[1]):
            #     st.append(p)
        return counts

            