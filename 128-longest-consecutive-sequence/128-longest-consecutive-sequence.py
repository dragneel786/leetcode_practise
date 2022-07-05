class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = dict()
        for n in nums:
            values[n] = values.get(n, 1)
        
        
        def traverse(val, dic):
            nonlocal counts
            num = val + dic
            while(num in values and values[num] != -1):
                values[num] = -1
                counts += 1
                num += dic
        
        longest = 0
        for n in nums:
            counts = 1
            traverse(n, -1)
            traverse(n,  1)
            longest = max(longest, counts)
        
        return longest
                
                
                
                