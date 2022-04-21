class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = defaultdict(int)
        for v in nums1:
            seen[v] += 1
        
        res = []
        for v in nums2:
            if(seen[v]):
                res.append(v)
                seen[v] -= 1
        
        return res
        
        
            