class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        lookup = defaultdict(lambda:False)
        for v in arr:
            if(lookup[(2 * v)] or lookup[(v / 2)]):
                return True
            lookup[v] = True
        return False