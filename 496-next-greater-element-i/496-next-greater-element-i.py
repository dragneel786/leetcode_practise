class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        if(n == 0):
            return []

        res = [] 
        lookup = defaultdict(lambda:-1)
        stack = deque()
        for i in range(n):
            while(len(stack) and stack[-1] < nums2[i]):
                lookup[stack.pop()] = nums2[i]

            stack.append(nums2[i])

        for n in nums1:
            res.append(lookup[n])

        return res