class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = [0] * 26
        n = len(s)
        for i in range(1, n):
            count[ord(s[i]) - 97] += 1


        s += '#'
        res = []
        seen = set(s[0])
        size = 1
        for i in range(1, n + 1):
            clear = True
            for k in seen:
                if(count[ord(k) - 97] != 0):
                    clear = False
                    break

            if(clear):
                res.append(size)
                size = 0
                seen.clear()

            if(s[i] == '#'):
                return res

            size += 1
            seen.add(s[i])
            count[ord(s[i]) - 97] -= 1