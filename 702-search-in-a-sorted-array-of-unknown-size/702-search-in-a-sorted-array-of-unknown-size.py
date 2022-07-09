# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        low = 0
        hval = (10 ** 4 + 1)
        high = hval
        while(low <= high):
            mid = ((high - low) >> 1) + low
            temp = reader.get(mid)
            if(temp == target):
                return mid
            
            if(temp > target):
                high = mid - 1
            else:
                low = mid + 1
        return -1
        