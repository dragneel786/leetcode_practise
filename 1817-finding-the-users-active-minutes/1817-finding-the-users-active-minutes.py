class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uam_map = defaultdict(set)
        for uid, time in logs:
            uam_map[uid].add(time)
        
        res = [0] * k
        for values in uam_map.values():
            size = len(values)
            res[size - 1] += 1
        
        return res
        
        
        