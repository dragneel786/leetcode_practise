class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def get_idx(indexes, idx):
            in_index = bisect_right(indexes, idx)
            if(in_index == len(indexes)):
                return indexes[0]
            return indexes[in_index]
        
        
        imap = defaultdict(list)
        for i, ch in enumerate(source):
            imap[ch].append(i)
            
        steps = 1
        curr_idx = -1
        for ch in target:
            if(ch not in imap):
                return -1
            
            idx = get_idx(imap[ch], curr_idx)
            steps += (curr_idx >= idx)
            curr_idx = idx
        
        return steps
            