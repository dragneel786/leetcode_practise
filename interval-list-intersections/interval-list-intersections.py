class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n1 = len(firstList)
        n2 = len(secondList) 
        if(not n1 or not n2):
            return []

        res = []
        i = 0
        j = 0
        while(i < n1 and j < n2):
            startMax = max(firstList[i][0], secondList[j][0])
            endMin = min(firstList[i][1], secondList[j][1])

            if(startMax <= endMin):
                res.append([startMax, endMin])

            if(endMin == firstList[i][1]):
                i += 1
            if(endMin == secondList[j][1]):
                j += 1


        return res