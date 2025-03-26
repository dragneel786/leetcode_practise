class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.idx_map = defaultdict(set)
        for i, num in enumerate(nums2):
            self.idx_map[num].add(i)

    def add(self, index: int, val: int) -> None:
        curr_val = self.nums2[index]
        self.nums2[index] += val
        self.idx_map[curr_val].remove(index)
        self.idx_map[curr_val + val].add(index)

    def count(self, tot: int) -> int:
        res = 0
        for val in self.nums1:
            if tot - val in self.idx_map:
                res += len(self.idx_map[tot - val])
        
        return res

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)