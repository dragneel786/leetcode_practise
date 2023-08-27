class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        @lru_cache(None)
        def can_cross(i, prev = 1, step = 1):
            if(i == n - 1):
                return True
            
            if(i >= n):
                return False
            
            new_step = prev + step - 1
            if(step - 1 > 0 and new_step in stone_map\
               and can_cross(stone_map[new_step], new_step, step - 1)):
                return True
            
            new_step = prev + step
            if(new_step in stone_map\
               and can_cross(stone_map[new_step], new_step, step)):
                return True
            
            new_step = prev + step + 1
            if(new_step in stone_map\
               and can_cross(stone_map[new_step], new_step, step + 1)):
                return True
        
            return False
                
        
        if(stones[0] + 1 != stones[1]):
            return False
        
        n = len(stones)
        stone_map = {s: i for i, s in enumerate(stones)}
        return can_cross(1)