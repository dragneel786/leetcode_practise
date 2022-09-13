class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        
        def count_ones(num):
            s = 128
            counts = 0
            while(s & num):
                s >>= 1
                counts += 1
            return counts

        ones = 0
        for i in range(len(data)):
            if(not ones):
                ones = count_ones(data[i])
                if(ones not in [0,2,3,4]):
                    return False
                if(ones): ones -= 1

            elif(count_ones(data[i]) == 1):
                ones -= 1

            else:
                return False

        return ones == 0

            
            
        
        
            