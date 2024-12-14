class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # [42,41,42,41,41,40,39,38]
        # minq: 39
        # maxq: 41, 41
        
        minq = deque()
        maxq = deque()
        res = start = 0
        for end in range(len(nums)):
            while(maxq and maxq[-1] < nums[end]):
                maxq.pop()
            
            while(minq and minq[-1] > nums[end]):
                minq.pop()
            
            minq.append(nums[end])
            maxq.append(nums[end])
            
            while(maxq[0] - minq[0] > 2):
                if maxq[0] == nums[start]:
                    maxq.popleft()
                
                if minq[0] == nums[start]:
                    minq.popleft()
                
                start += 1
            
            # print(f'minq: {minq}, maxq: {maxq}, start: {start}, end: {end}')
            res += end - start + 1
          
        return res
        
        
        