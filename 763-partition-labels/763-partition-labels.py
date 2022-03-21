class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = defaultdict(int)
        n = len(s)
        for i in range(n):
            hash[s[i]] = i

        s += '#'
        res = []
        maxIdx = 0
        prev = -1
        for i in range(n + 1):
            maxIdx = max(maxIdx, hash[s[i]])
            if(i == maxIdx):
                res.append(maxIdx - prev)
                prev = maxIdx
                maxIdx = hash[s[i]]

            if(i == n):
                return res