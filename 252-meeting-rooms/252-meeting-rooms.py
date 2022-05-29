class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        size = 0
        for i in intervals:
            size = max(i[1], size)
        
        if(not size):
            return True
        inter = [0] * (size + 2)
        for i in intervals:
            inter[i[1]] += -1
            inter[i[0]] += 1
        
        for i in range(1, size):
            inter[i] += inter[i - 1]
            if(inter[i] > 1):
                return False
        
        return True
                