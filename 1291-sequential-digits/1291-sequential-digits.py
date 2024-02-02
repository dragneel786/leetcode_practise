class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        def get_start(size, init = 1):
            nonlocal low
            val = init
            if(init + size - 1 > 9):
                val = 1
                size += 1
            for _ in range(size - 1):
                val = (val * 10) + ((val % 10) + 1)
            return (size, val) if(val >= low) else get_start(size, init + 1)

        res = []
        s_size = len(str(low))
        s_size, start = get_start(s_size, int(str(low)[0]))
        while(start <= high and s_size <= 9):
            res.append(start)
            if(start % 10 == 9):
                s_size += 1
                _, start = get_start(s_size)
            else:
                start = (int(str(start)[1:]) * 10) + ((start % 10) + 1)

        return res

