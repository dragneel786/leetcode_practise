class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kth = []
        n = len(nums)
        for i in range(k):
            kth.append(nums[i])
        
        heapify(kth)
        for i in range(k, n):
            if(kth[0] < nums[i]):
                heappop(kth)
                heappush(kth, nums[i])
        
        return kth[0]
        