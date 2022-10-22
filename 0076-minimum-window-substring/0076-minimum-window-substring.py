class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        sn, tn = len(s), len(t)
        if(sn < tn): return ''
        min_index = lambda x, y: x if(abs(x[1] - x[0]) <\
                                        abs(y[1] - y[0])) else y
        covered = lambda a, b: True if(not a - b) else False

        def create_indexes(s, counts):
            indexes = deque()
            for i, c in enumerate(s):
                if(c in counts):
                    indexes.append(i)

            return indexes


        def assign_index(left, right):
            nonlocal ans_index
            if(not ans_index):
                ans_index = (left, right)
            else:
                ans_index = min_index(ans_index,\
                                        (left, right))

        tcount = Counter(t)
        sindex = create_indexes(s, tcount)

        right, ans_index = 0, None
        curr_window = Counter()

        while(sindex):
            while(not covered(tcount, curr_window)\
                    and right < sn):
                if(s[right] in tcount):
                    curr_window[s[right]] += 1
                right += 1

            if(covered(tcount, curr_window)):
                assign_index(sindex[0], right)

            curr_window[s[sindex.popleft()]] -= 1

        return s[ans_index[0]: ans_index[1]] if(ans_index) else ''





