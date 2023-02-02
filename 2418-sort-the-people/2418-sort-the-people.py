class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nh = {h:n for n, h in zip(names, heights)}
        return [nh[h] for h in sorted(heights, reverse=True)]