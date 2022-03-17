class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def getBitCount():
            res = []
            for a in arr:
                count = 0
                while(a):
                    a &= (a - 1)
                    count += 1
                res.append(count)

            return res

        bits = getBitCount()
        for i in range(1, len(arr)):
            j = i - 1
            bit = bits[i]
            val = arr[i]
            while(j > -1 and (bits[j] > bit or (bits[j] == bit and arr[j] > val))):
                bits[j + 1] = bits[j]
                arr[j + 1] = arr[j]
                j -= 1

            bits[j + 1] = bit
            arr[j + 1] = val

        return arr
                
        