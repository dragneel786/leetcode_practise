class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        res = (math.inf, 0, 0)
        req = len(target)

        window = defaultdict(lambda:0)
        formed = 0
        l, r = 0, 0
        n = len(s)
        while(r < n):
            ch = s[r]
            window[ch] += 1

            if(ch in target and target[ch] == window[ch]):
                formed += 1

            while(l <= r and formed == req):
                ch = s[l]

                if((r - l + 1) < res[0]):
                    res = ((r - l + 1), l, r)

                if(ch in target and target[ch] == window[ch]):
                    formed -= 1

                window[ch] -= 1
                l += 1
            r += 1

        return s[res[1]: res[2] + 1] if(res[0] != math.inf) else ""
                
                