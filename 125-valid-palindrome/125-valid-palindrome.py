class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = (''.join(filter(lambda c: c.isalnum(), s))).lower()
        return temp == temp[::-1]