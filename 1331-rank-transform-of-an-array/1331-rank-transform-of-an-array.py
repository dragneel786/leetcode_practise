class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        indexes = defaultdict(list)
        for i, val in enumerate(arr):
            indexes[val].append(i)
        
        curr_rank = 0
        ranks = [0] * len(arr)
        for v in sorted(indexes.keys()):
            curr_rank += 1
            for i in indexes[v]:
                ranks[i] = curr_rank

        return ranks
        