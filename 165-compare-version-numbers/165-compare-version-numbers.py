class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split(".")))
        version2 = list(map(int, version2.split(".")))
        i, j = 0, 0
        m, n = len(version1), len(version2)
        while(i < m or j < n):
            val1 = version1[i] if i < m else 0
            val2 = version2[j] if j < n else 0
            i += 1
            j += 1
            if(val1 > val2):
                return 1
            if(val1 < val2):
                return -1
        
        return 0