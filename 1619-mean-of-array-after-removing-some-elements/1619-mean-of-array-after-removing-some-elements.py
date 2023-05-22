class Solution:
    def trimMean(self, arr: List[int]) -> float:
        size = len(arr)
        per = int(size * 0.05)
        arr.sort()
        return sum(arr[per: size - per]) / (size - per * 2)
            