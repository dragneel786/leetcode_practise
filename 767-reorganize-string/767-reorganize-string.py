class Solution:
    def reorganizeString(self, s: str) -> str:
        a = sorted(sorted(s), key=s.count)
        h = len(a) // 2
        a[1::2], a[::2] = a[:h], a[h:]
        return ''.join(a) * (a[-1:] != a[-2:-1])
            
            