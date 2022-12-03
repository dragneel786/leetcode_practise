class Solution:
    def frequencySort(self, s: str) -> str:
        count = [(c, v) for c, v in Counter(s).items()]
        return ''.join([c * v for c, v in sorted(count, key=lambda x:-x[1])])
        