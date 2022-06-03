class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if(n - 1 <= k):
            return n

        maxL = k + 1
        first = Counter(s[0:maxL])
        count = max(first.values())
        for w in range(k + 2, n + 1):
            if(w <= n):
                first[s[w - 1]] = first.get(s[w - 1], 0) + 1
                count = max(first[s[w - 1]], count)
            look, c = first.copy(), count
            for j in range(n - w + 1):
                if(w - c <= k):
                    maxL = w
                    break
                look[s[j]] -= 1
                if(j + w < n):
                    look[s[j + w]] += 1
                    c = max(look[s[j + w]], c)
            if(w != maxL):
                break
        return maxL