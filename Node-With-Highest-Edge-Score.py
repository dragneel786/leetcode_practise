class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        score = [0] * len(edges)
        for i, e in enumerate(edges):
            score[e] += i
        
        max_idx, max_score = 0, 0
        for idx, score in enumerate(score):
            if score > max_score:
                max_idx = idx
                max_score = score

        return max_idx