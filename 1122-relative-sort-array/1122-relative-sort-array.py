class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        res = []
        for a in arr2:
            res.extend([a] * counter[a])
            del counter[a]
        
        return res + sorted([a for a, c in counter.items() for _ in range(c)])