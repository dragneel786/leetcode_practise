class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        uc = Counter(set(nums1))
        uc += Counter(set(nums2))
        uc += Counter(set(nums3))
        return [k for k, v in uc.items() if v >= 2]
        