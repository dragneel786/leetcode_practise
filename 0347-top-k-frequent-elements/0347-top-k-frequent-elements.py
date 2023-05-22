class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = [(c, v) for v, c in Counter(nums).items()]
        counter.sort()
        return [counter.pop()[1] for _ in range(k)]