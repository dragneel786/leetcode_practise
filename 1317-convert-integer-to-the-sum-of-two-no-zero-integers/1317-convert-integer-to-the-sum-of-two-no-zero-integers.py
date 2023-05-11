class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n + 1):
            if('0' not in f'{n - i}{i}'):
                return [i, n - i]