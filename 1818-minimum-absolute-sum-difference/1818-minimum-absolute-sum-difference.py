class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        diff = [abs(nums1[i] - nums2[i]) for i in range(n)]
        nums1.sort()
        best_ = -math.inf
        for i in range(n):
            lb = bisect_left(nums1, nums2[i])
            if(lb >= n):
                lb = n - 1
            val = min(abs(nums1[lb - 1] - nums2[i]), abs(nums1[lb]- nums2[i]))
            if(best_ < (diff[i] - val)):
                best_ = (diff[i] - val)
                pos = val

        return (sum(diff) - best_) % (10 ** 9 + 7)