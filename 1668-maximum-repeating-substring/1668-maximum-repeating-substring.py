class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        
        n = len(sequence)
        count = 0
        wn = len(word)
        for i in range(n - wn + 1):
            temp_count = k = 0
            
            while(word == sequence[i + k: i + k + wn]):
                k += wn
                temp_count += 1
                    
            count = max(temp_count, count)
            
        return count
                