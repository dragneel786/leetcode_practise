class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        val = min(k, numOnes)
        k -= val
        
        if(k > 0):
            val += 0 * min(k, numZeros)
            k -= min(k, numZeros)
        
        if(k > 0):
            val += -1 * min(k, numNegOnes)
        
        return val