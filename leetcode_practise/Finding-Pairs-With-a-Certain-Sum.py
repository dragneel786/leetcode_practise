class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

        self.nums2_index_map = defaultdict(set)
        for i, num in enumerate(nums2):
            self.nums2_index_map[num].add(i)
        
    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        self.nums2[index] += val
        new_val = self.nums2[index]

        self.nums2_index_map[old_val].remove(index)
        self.nums2_index_map[new_val].add(index)

    def count(self, tot: int) -> int:
        counts = 0
        for num in self.nums1:
            counts += len(self.nums2_index_map[tot - num])
        return counts


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)