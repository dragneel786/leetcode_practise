class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for row in image:
            for j in range((n + 1) // 2):
                if(j == n - j - 1):
                    row[j] ^= 1
                else:
                    row[j], row[n - j - 1] = row[n - j - 1] ^ 1, row[j] ^ 1
        return image
        
                
                
                