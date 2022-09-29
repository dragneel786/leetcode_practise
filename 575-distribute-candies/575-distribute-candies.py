class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        can_eat = len(candyType) // 2
        type_size = len(Counter(candyType))
    
        return type_size if(can_eat > type_size) else can_eat
        
        
        
        