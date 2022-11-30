class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = set()
        for c in Counter(arr).values():
            if(c in s):
                return False
            s.add(c)
        return True