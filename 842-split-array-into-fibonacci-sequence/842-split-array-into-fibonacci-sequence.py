class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:

        def getList(num, res, op = []):
            upper_bound = 2**31
            if(not num):
                if(len(op) >= 3):
                    res.append(op[:])
                return

            val = 0
            for i in range(len(num)):
                val = val * 10 + int(num[i])
                if(val < upper_bound):
                    if(len(op) < 2):
                        getList(num[i + 1:], res, op + [val])
                    elif(val == op[-1] + op[-2]):
                        getList(num[i + 1:], res, op + [val])

                if(num[i] == '0' and val == 0):
                    return 

        res = []
        getList(num, res)
        return res[0] if res else []