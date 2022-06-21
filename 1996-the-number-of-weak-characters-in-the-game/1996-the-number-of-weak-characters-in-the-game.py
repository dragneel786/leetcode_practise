class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: [-x[0], x[1]])
        n = len(properties)
        counts = 0
        maxi = 0
        for i in range(n):
            p = properties[i]
            if(p[1] < maxi):
                counts += 1
            maxi = max(maxi, p[1])
        return counts

            