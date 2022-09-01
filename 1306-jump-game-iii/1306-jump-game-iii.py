class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        def reach_zero(index, visited = set()):
            if(index < 0 or index >= len(arr)\
               or index in visited):
                return False
            
            if(not arr[index]):
                return True
            
            visited.add(index)
            return reach_zero(index + arr[index], visited)\
        or reach_zero(index - arr[index], visited)
        
        return reach_zero(start)