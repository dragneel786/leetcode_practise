class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        
        max_bucket = max(counts.values())
        buckets = [0] * (max_bucket + 1)
        
        for c in counts.values():
            buckets[c] += 1
        
        
        needed_to_remove = len(arr) // 2
        set_size= 0
        while(needed_to_remove > 0):
            needed_from_bucket = ceil(needed_to_remove / max_bucket)
            set_size_added = min(buckets[max_bucket], needed_from_bucket)
            needed_to_remove -= set_size_added * max_bucket
            set_size += set_size_added
            max_bucket -= 1
        
        return set_size