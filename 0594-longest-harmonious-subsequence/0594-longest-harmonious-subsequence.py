class Solution:
    def findLHS(self, nums: List[int]) -> int:
        l = 0
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
            
            if(hashmap[num + 1]):
                l = max(l, hashmap[num + 1] + hashmap[num])
                
            if(hashmap[num - 1]):
                l = max(l, hashmap[num - 1] + hashmap[num])
        
        return l