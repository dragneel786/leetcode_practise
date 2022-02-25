class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        m = len(version1)
        n = len(version2)
        i = 0
        j = 0
        while(i < m or j < n):
            val1 = 0
            val2 = 0
            while(i < m and version1[i] != "."):
                val1 = (val1 * 10) + int(version1[i])
                i += 1
            i += 1

            while(j < n and version2[j] != "."):
                val2 = (val2 * 10) + int(version2[j])
                j += 1
            j += 1

            if(val1 < val2):
                return -1

            if(val1 > val2):
                return 1

        return 0