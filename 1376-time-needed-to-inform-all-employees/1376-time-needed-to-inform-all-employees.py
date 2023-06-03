class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        def populate(src):
            if(time[src] != -1):
                return time[src]
            
            time[src] = populate(manager[src])\
            + informTime[manager[src]]
            return time[src]
        
        time = [-1] * n
        time[headID] = 0
        for i in range(n):
            time[i] = populate(i)
        
        return max(time)
        
                
                
                
        
    