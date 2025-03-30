class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        idx_map = [0] * n
        min_idx = Counter()
        for i, c in enumerate(s):
            if c in min_idx:
                idx_map[i] = min_idx[c]
            else:
                idx_map[i] = i
                min_idx[c] = i
        
        curr_counts = 0
        min_idx = inf
        res = []
        print(idx_map)
        for i in range(n - 1, -1, -1):
            min_idx = min(min_idx, idx_map[i])
            curr_counts += 1
            if i == min_idx:
                res.append(curr_counts)
                curr_counts = 0
        
        return res[::-1]

