class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(not nums):
            return 0
        
        seen = defaultdict(lambda:False)
        for n in nums:
            seen[n] = True
        
        longest = 0
        for n in nums:
            if(seen[n]):
                f = n - 1
                c1 = 0
                while(seen[f]):
                    seen[f] = False
                    f -= 1
                    c1 += 1

                f = n + 1
                c2 = 0
                while(seen[f]):
                    seen[f] = False
                    f += 1
                    c2 += 1
                
                longest = max(c1 + c2 + 1, longest)
        
        return longest