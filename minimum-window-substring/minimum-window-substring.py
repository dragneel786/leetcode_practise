class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def get_ans(ans, word):
            if(ans and len(ans) <= len(word)):
                return ans
            return word

        left = 0
        tmap = Counter(t)
        smap = Counter()
        ans = None

        for right, c in enumerate(s):
            smap[c] += 1

            while(not tmap - smap):
                smap[s[left]] -= 1
                if(not smap[s[left]]): del smap[s[left]]
                ans = get_ans(ans, s[left: right + 1])
                left += 1

        return ans if(ans) else ''