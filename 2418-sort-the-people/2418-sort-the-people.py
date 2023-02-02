class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        nh = [(h, n) for n, h in zip(names, heights)]
        return [n for _, n in sorted(nh, reverse=True)]