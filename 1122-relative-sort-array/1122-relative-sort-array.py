class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        k = {a: i for i, a in enumerate(arr2)}
        return sorted(arr1, key=lambda a: k.get(a, 1000+a))