class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ls = {i: c for i, c in zip(indices, s)}
        return ''.join([ls[i] for i in range(len(s))])