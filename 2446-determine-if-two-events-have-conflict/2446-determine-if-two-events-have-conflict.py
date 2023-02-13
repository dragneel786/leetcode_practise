class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def time_in_mins(val):
            hh, mm = val.split(':')
            return int(hh) * 60 + int(mm)
            
    
        
        for i in range(2):
            event1[i] = time_in_mins(event1[i])
            event2[i] = time_in_mins(event2[i])
        
        print(event1, event2)
        return event1[0] <= event2[0] <= event1[1]\
    or event1[0] <= event2[1] <= event1[1]\
    or event2[0] <= event1[0] <= event2[1]\
    or event2[0] <= event1[1] <= event2[1]
        
        
        