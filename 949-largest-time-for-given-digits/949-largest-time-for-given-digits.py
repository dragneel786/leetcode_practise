class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        def possible():
            temp = None
            for m in range(60):
                m1, m2 = m // 10, m % 10
                if(arr[m1]):
                    arr[m1] -= 1
                    if(arr[m2]):
                        temp = str(m1) + str(m2)
                    arr[m1] += 1
            return temp
        
        arr = Counter(arr)
        res = ""
        for h in range(24):
            d1, d2 = h // 10, h % 10
            if(arr[d1]):
                arr[d1] -= 1
                if(arr[d2]):
                    arr[d2] -= 1
                    v = possible()
                    if(v):
                        res = str(d1) + str(d2) + ":" + v
                    arr[d2] += 1
                arr[d1] += 1
        return res
                    
                    
        
        
        
        
                