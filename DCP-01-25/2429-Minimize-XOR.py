class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_rating_map = defaultdict(tuple)
        self.cuisine_food_map = defaultdict(list)
        
        for c, f, r in zip(cuisines, foods, ratings):
            self.cuisine_food_map[c].append((-r, f))
            self.food_rating_map[f] = (-r, c)
            
        for k in self.cuisine_food_map.keys():
            heapify(self.cuisine_food_map[k])
        
        # print(self.food_rating_map, self.cuisine_food_map)

    def changeRating(self, food: str, newRating: int) -> None:
        ra, cu = self.food_rating_map[food]
        self.food_rating_map[food] = (-newRating, cu)
        heappush(self.cuisine_food_map[cu], (-newRating, food))
        
    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_food_map[cuisine]
        while(heap[0][0] != self.food_rating_map[heap[0][1]][0]):
            heappop(heap)
        
        return heap[0][1]
            
        
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)