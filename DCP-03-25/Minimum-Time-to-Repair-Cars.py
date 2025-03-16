class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_possible(repair_time):
            tot = 0
            for v in ranks:
                tot += floor(sqrt(repair_time // v))

            return tot >= cars


        low, high = 1, max(ranks) * cars * cars
        res = 0
        while(low <= high):
            middle = low + (high - low) // 2
            if is_possible(middle):
                res = middle
                high = middle - 1
            else:
                low = middle + 1
        
        return res