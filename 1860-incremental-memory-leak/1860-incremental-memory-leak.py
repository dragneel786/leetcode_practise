class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        curr_time = 1
        while(curr_time <= memory1 or curr_time <= memory2):
            if(memory1 >= memory2):
                memory1 -= curr_time
            else:
                memory2 -= curr_time
            
            curr_time += 1
        
        return [curr_time, memory1, memory2]