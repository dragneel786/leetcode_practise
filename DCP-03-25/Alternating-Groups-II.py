class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        res = start = alternates = 0
        colors = colors + colors[:k - 1]
        for end in range(1, len(colors)):
            if colors[end] != colors[end - 1]:
                alternates += 1

            if end >= k:
                alternates -= colors[start] != colors[start + 1]
                start += 1

            if end >= k - 1 and alternates >= k - 1:
                res += 1

        return res





