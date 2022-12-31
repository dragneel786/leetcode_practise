class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        values = [(freq[num], num) for num in nums]
        return [a for _, a in sorted(values, key=lambda k: [k[0], -k[1]])]