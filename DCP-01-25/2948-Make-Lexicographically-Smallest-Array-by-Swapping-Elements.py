class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        size = len(nums) 
        nums_sort = sorted(nums)
        q = deque([nums_sort[0]]) 
        curr, num_mapping, group_mapping = 0, {nums_sort[0]: 0}, {0: q}  

        for i in range(size - 1):
            if nums_sort[i + 1] - nums_sort[i] > limit: 
                curr += 1
                q = deque()

            q.append(nums_sort[i + 1])
            num_mapping[nums_sort[i + 1]] = curr
            group_mapping.setdefault(curr, q)
        
        for i in range(size):
            nums[i] = group_mapping[num_mapping[nums[i]]].popleft()

        return nums
            
                
