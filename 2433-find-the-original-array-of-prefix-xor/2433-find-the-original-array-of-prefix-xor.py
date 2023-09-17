class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        xor = 0
        prev = pref[0]
        for i in range(1, len(pref)):
            prev, pref[i] = pref[i], pref[i] ^ prev
        
        return pref