class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1),
                      (1,1),(1,-1),(-1,1),(-1,-1)]:
            nx, ny = king
            while(0 <= nx < 8 and 0 <= ny < 8):
                if([nx, ny] in queens):
                    ans.append([nx, ny])
                    break
                
                nx += dr
                ny += dc
        
        return ans
            