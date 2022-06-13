class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start, end = list(start), list(end)
        n = len(start)
        i = 0 
        while(i < n):
            if(end[i] != start[i]):
                if(i < n - 1 and end[i] == "L" and start[i] == "X"):
                    j = i + 1
                    while(j < n and start[j] == "X"):
                        j += 1
                    if(j < n and start[j] == "L"):
                        start[i], start[j] = start[j], start[i]

                elif(i < n - 1 and end[i] == "X" and start[i] == "R"):
                    j = i + 1
                    while(j < n and start[j] == "R"):
                        j += 1
                    if(j < n and start[j] == "X"):
                        start[i], start[j] = start[j], start[i]
                else:
                    return False
            i += 1

        return start == end



