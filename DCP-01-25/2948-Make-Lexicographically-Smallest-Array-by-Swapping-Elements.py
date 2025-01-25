class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        def union(x, y):
            px, py = find(x), find(y)
            parent[py] = px

        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return x

        size = len(nums) 
        nums_sort = sorted(nums)
        parent = {num:num for num in nums}
        ques = {}
        q, curr = deque([nums_sort[0]]), nums_sort[0]
        for i in range(size - 1):
            if nums_sort[i + 1] - nums_sort[i] <= limit: 
                union(nums_sort[i], nums_sort[i + 1])
                q.append(nums_sort[i + 1])
            else:
                ques[curr] = q
                q = deque([nums_sort[i + 1]])
                curr = nums_sort[i + 1]
        
        
        ques[curr] = q
        # print(parent, ques)
        for i in range(size):
            # print(nums[i], ques[find(nums[i])])
            nums[i] = ques[find(nums[i])].popleft()

        return nums
                
