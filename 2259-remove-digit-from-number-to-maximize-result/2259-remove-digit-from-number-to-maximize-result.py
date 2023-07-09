class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        last_idx = -1
        number += '0'
        for i in range(1, len(number)):
            if(number[i - 1] == digit):
                last_idx = i - 1
                if(number[i - 1] < number[i]):
                    return number[:i - 1] + number[i:-1]
                
        return number[:last_idx] + number[last_idx + 1:-1]