class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        keys = Counter(arr).values()
        return len(keys) == len(set(keys))