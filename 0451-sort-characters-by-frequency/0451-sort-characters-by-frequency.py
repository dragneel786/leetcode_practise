class Solution:
    def frequencySort(self, s: str) -> str:
        bucket = defaultdict(list)
        for c, v in Counter(s).items():
            bucket[v].append(c)
            
        return ''.join([k * a for k in range(len(s), 0, -1)\
                        for a in bucket[k]])
        