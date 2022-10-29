class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        pg = [(p, g) for p, g in zip(plantTime, growTime)]
        pg.sort(key=lambda x: -x[1])
        
        ans, gb = pg[0]
        gb += 1
        for p, g in pg[1:]:
            ans += p
            gb -= p
            gb = max(gb, g + 1)
            
        return ans + gb - 1
            