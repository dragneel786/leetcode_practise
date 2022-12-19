class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people = {i for i in range(1, n + 1)}
        tcount = defaultdict(int)
        
        for a, b in trust:
            people.discard(a)
            tcount[b] += 1
        
        if(len(people) != 1):
            return -1
        
        val = list(people)[0]
        if(tcount[val] == n - 1):
            return val
        
        return -1 