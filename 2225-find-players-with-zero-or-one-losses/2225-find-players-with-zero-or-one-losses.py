class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose_count = defaultdict(int)
        for a, b in matches:
            lose_count[b] += 1
            lose_count[a] = lose_count.get(a, 0)
            
        zeros = []
        ones = []
        for p, c in lose_count.items():
            if(c == 0):
                zeros.append(p)
            
            if(c == 1):
                ones.append(p)
        
        return [sorted(zeros), sorted(ones)]
            
        