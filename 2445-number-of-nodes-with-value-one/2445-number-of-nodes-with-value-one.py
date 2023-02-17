class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        def update(start, add = 0):
            if(start > n):
                return
            
            nodes[start] += add
            update(start * 2, nodes[start])
            update(start * 2 + 1, nodes[start])
            
        nodes = [0] * (n + 1)
        for q in queries:
            nodes[q] += 1
        update(1)
        return sum([num % 2 for num in nodes])