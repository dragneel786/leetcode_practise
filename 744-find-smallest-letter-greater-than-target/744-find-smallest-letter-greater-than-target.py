class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in range(1, 26):
            low = 0
            high = len(letters) - 1
            ch = chr((((ord(target) - 97) + i) % 26) + 97)
            print(ch)
            while(low <= high):
                mid = low + (high - low) // 2
                if(letters[mid] == ch):
                    return ch
            
                if(ch < letters[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
        