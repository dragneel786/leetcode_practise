class Solution:
    def hammingWeight(self, n: int) -> int:
        if(not n):
            return n
        count = 1
        while n := n & n - 1: count += 1
        return count