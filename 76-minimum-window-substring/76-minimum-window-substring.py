class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tmap = Counter(t)
        cindex = [(i, c) for i, c in\
             enumerate(s) if(c in tmap)]
        if(not cindex): return ''
        
        smap = Counter()

        needed = len(tmap)
        made = left = 0
        ans = (inf, None, None)

        for index, char in cindex:
            smap[char] += 1
            if(smap[char] == tmap[char]):
                made += 1

            previ, prevc = cindex[left]
            while(smap[prevc] >= tmap[prevc] and made == needed):
                if(ans[0] > index - previ + 1):
                    ans = (index - previ + 1, previ, index)

                smap[prevc] -= 1
                if(smap[prevc] < tmap[prevc]):
                    made -= 1

                left += 1
                if(left >= len(cindex)):
                    break
                previ, prevc = cindex[left]

        return s[ans[1]: ans[2] + 1] if(ans[0] != inf) else ''