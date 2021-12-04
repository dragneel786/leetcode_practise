def floodFill(image, sr: int, sc: int, newColor: int):  
        color = image[sr][sc]
        visited = set()
        def fill(image, sr: int, sc: int, newColor: int):
            if (sr >= len(image) or sc >= len(image[0]) \
                or sr < 0 or sc < 0 or color != image[sr][sc] or (sr, sc) in visited):
                return

            image[sr][sc] = newColor
            visited.add((sr, sc))
            fill(image, sr + 1, sc, newColor)
            fill(image, sr, sc + 1, newColor)
            fill(image, sr - 1, sc, newColor)
            fill(image, sr, sc - 1, newColor)
        
        fill(image, sr, sc, newColor)
        return image

print(floodFill([[0,0,0],[0,1,1]], 1, 1, 1))
    