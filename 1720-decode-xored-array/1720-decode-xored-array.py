class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        return accumulate([first] + encoded, lambda a, b: a ^ b)