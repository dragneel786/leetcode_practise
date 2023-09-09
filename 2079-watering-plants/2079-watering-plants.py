class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cap = capacity
        steps = 0
        for i, plant in enumerate(plants):
            if(cap < plant):
                steps += (i * 2)
                cap = capacity
            
            steps += 1
            cap -= plant
        
        return steps
            