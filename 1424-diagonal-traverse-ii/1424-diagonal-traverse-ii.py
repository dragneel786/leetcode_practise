class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        dig = defaultdict(list)
        order = deque([i for i in range((10 ** 5) + 2)])
        for r in range(len(nums)):
            idx = 0
            for v in nums[r]:
                dig[order[idx]].append(v)
                idx += 1
            
            order.popleft()
        
        for i in range((10 ** 5) + 2):
            if(i not in dig):
                break
            
            ans.extend(reversed(dig[i]))
            
        return ans
        