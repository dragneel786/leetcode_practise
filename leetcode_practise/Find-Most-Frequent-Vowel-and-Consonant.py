class Solution:
    def maxFreqSum(self, s: str) -> int:
        counts = Counter(s)
        vowels = 'aeiou'
        return max([0] + [v for k, v in counts.items()\
         if k in vowels]) +  \
         max([0] + [v for k, v in counts.items()\
          if k not in vowels])

