class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vers1 = version1.split(".")
        vers2 = version2.split(".")
        for a, b in zip_longest(vers1, vers2, fillvalue='0'):
            a = int(a)
            b = int(b)
            if a > b:
                return 1
            
            if a < b:
                return -1
        
        return 0
        

        

        

