class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        def generate_number(num = 0):
            if(len(str(num)) == n):
                result.append(num)
                return
            
            start = 0 if(num) else 1
            
            for v in range(start, 10):
                if(not num or abs(num % 10 - v) == k):
                    generate_number(num * 10 + v)
        
        result = []
        generate_number()
        return result
        