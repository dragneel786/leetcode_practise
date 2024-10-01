class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        hash_map = Counter()
        for a in arr:
            map_val = ((a % k) + k) % k
            hash_map[map_val] += 1
        
        for i in range(k):
            if (i == 0 and hash_map[i] % 2 == 0) or\
            (hash_map[i] == hash_map[k - i]):
                continue
            
            else:
                return False
        
        return True
                