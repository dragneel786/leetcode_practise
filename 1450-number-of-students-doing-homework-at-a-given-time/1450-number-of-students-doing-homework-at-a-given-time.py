class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        counts = 0
        for s, e in zip(startTime, endTime):
            if(s <= queryTime 
               and e >= queryTime):
                counts += 1
        
        return counts