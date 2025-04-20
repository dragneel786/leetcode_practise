class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = Counter(answers)
        res = 0
        for k, v in counts.items():
            while(v > 0):
                v -= k + 1
                res += k + 1

        return res
