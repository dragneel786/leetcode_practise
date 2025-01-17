class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
        def is_formable(start = 0):
            curr = start
            for v in derived:
                curr = curr ^ v
                
            return curr == start

        return is_formable(0) or is_formable(1)
        