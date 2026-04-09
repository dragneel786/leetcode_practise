class Solution:
    def countCommas(self, n: int) -> int:
        if n <= 999:
            return 0

        if n <= 9999:
            return n - 999
        
        if n <= 99999:
            return (n - 9999) + 9000
        
        if n <= 999999:
            return (n - 99999) + 99000