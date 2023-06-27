class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1 = len(nums1)
        n2 = len(nums2)
        ans = []
        visited = set([(0, 0)])
        min_heap = [(nums1[0] + nums2[0], 0, 0)]
        
        while(k > 0 and min_heap):
            val, i, j = heappop(min_heap)
            ans.append([nums1[i], nums2[j]])
            
            if i + 1 < n1 and (i + 1, j) not in visited:
                heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            
            if j + 1 < n2 and (i, j + 1) not in visited:
                heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
            k -= 1
        
        return ans
        
                         