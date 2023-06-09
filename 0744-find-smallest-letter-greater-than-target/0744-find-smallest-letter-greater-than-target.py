class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low = 0
        high = len(letters) - 1
        if(letters[-1] > target and target != 'z'):
            while(low < high):
                mid = low + (high - low) // 2
                if target >= letters[mid]:
                    low = mid + 1
                else:
                    high = mid

        return letters[low]