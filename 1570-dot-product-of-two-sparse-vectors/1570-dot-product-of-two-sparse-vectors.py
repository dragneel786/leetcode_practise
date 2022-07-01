class SparseVector:
    def __init__(self, nums: List[int]):
        self.v = defaultdict(lambda:0)
        for i,n in enumerate(nums):
            if(n):
                self.v[i] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        v1, res = self.v, 0
        v2 = vec.v
        for i in v2.keys():
            res += (v1[i] * v2[i])
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)