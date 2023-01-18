class Solution:
    def sortString(self, s: str) -> str:
        scounts = Counter(s)
        keys = list(sorted(scounts.keys()))
        ans = []
        while(scounts):
            for c in ascii_lowercase + ascii_lowercase[::-1]:
                if(scounts[c]):
                    ans.append(c)
                    scounts[c] -= 1
                    if(not scounts[c]):
                        del scounts[c]
        
        return ''.join(ans)

            