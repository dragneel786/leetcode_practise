class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        first = [s1[0], s1[2]]
        second = [s2[0], s2[2]]
        third = [s1[1], s1[3]]
        four = [s2[1], s2[3]]
        return sorted(first) == sorted(second) \
    and sorted(third) == sorted(four)