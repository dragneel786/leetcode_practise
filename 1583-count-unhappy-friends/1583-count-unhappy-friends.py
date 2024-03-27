class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        def check(a, b):
            for p in preferences[a]:
                if(p == b):
                    break
                
                p_pair = pair_with[p]
                if(perf_idx[p][a] < perf_idx[p][p_pair]):
                    return True
                
            return False
                
        pair_with = dict()
        for a, b in pairs:
            pair_with[a] = b
            pair_with[b] = a
            
        perf_idx = dict()
        for i, perf in enumerate(preferences):
            for j, p in enumerate(perf):
                perf_idx.setdefault(i, dict())
                perf_idx[i][p] = j
        
        
        ans = 0
        for a, b in pairs:
            ans += check(a, b)
            ans += check(b, a)
            # print(check(a, b), check(b, a))
        
        return ans
        
        