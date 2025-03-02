class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        sum_ids = Counter()
        for id1, val in nums1:
            sum_ids[id1] += val

        for id2, val in nums2:
            sum_ids[id2] += val

        res = []
        for k, v in sum_ids.items():
            res.append([k, v])

        return sorted(res)

