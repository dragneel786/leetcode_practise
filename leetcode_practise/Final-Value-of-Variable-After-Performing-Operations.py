class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        val = 0
        for ops in operations:
            if '+' in ops:
                val += 1
            else:
                val -= 1
        
        return val
