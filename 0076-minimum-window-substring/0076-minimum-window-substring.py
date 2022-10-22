class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        sn, tn = len(s), len(t)
        if(sn < tn): return ''
        covered = lambda a, b: True if(not a - b) else False

        def assign_index(left, right):
            nonlocal ans_index
            new_index = (left, right, right - left)
            if(not ans_index):
                ans_index = new_index
            else:
                ans_index = min(new_index,\
                     ans_index, key=lambda x:x[2])

        tcount = Counter(t)
        sindex = deque()

        right, ans_index = 0, None
        scount = Counter()
        
        while(right < sn):
            if(right < sn and s[right] in tcount):
                scount[s[right]] += 1
                sindex.append(right)
            right += 1

            while(not len(tcount - scount)):
                assign_index(sindex[0], sindex[-1] + 1)
                scount[s[sindex.popleft()]] -= 1

        return s[ans_index[0]: ans_index[1]] if(ans_index) else ''





