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
        curr_window = Counter()
        
        while(right < sn):
            if(right < sn and s[right] in tcount):
                curr_window[s[right]] += 1
                sindex.append(right)
            right += 1

            while(covered(tcount, curr_window)):
                assign_index(sindex[0], sindex[-1] + 1)
                curr_window[s[sindex.popleft()]] -= 1

        return s[ans_index[0]: ans_index[1]] if(ans_index) else ''





