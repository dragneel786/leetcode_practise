class Solution:
    def maximumSwap(self, num: int) -> int:
        values = list(map(int, list(str(num))))
        for i in range(len(values)):
            maxed = values[i]
            idx = i
            for j in range(i + 1, len(values)):
                if maxed <= values[j]:
                    maxed = values[j]
                    idx = j
            
            if maxed > values[i]:
                values[i], values[idx] = values[idx], values[i]
                break
                    
        return int(''.join(map(str, values)))