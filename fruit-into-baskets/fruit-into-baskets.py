class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        fruits_order = OrderedDict()
        left = 0
        for right, fruit in enumerate(fruits):
            
            if(fruit in fruits_order):
                del fruits_order[fruit]
                
            fruits_order[fruit] = right
            
            if(len(fruits_order) > 2):
                _, left = fruits_order.popitem(0)
                left += 1
            
            max_fruits = max(max_fruits, right - left + 1)
        
        return max_fruits