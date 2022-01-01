class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1 = len(s)
        n2 = len(p)
        if(n1 < n2):
            return []
        res = []
        window = [0] * 26
        target = [0] * 26
        for i in range(n2):
            window[ord(s[i]) - 97] += 1
            target[ord(p[i]) - 97] += 1

        if(target == window):
            res.append(0)

        for i in range(1, n1 - n2 + 1):
            window[ord(s[i - 1]) - 97] -= 1
            window[ord(s[i + n2 - 1]) - 97] += 1

            if(window == target):
                res.append(i)

        return res