class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index_map = defaultdict(list)
        for i,num in enumerate(nums2):
            index_map[num].append(i)
        
        res = []
        for num in nums1:
            res.append(index_map[num].pop())
        
        return res
            