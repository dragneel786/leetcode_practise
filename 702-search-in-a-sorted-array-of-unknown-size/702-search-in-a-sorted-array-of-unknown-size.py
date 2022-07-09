# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        lo, hi = 0, 1
        while(reader.get(hi) < target):
            lo = hi
            hi <<= 1
    
        while(lo <= hi):
            mid = ((hi - lo) >> 1) + lo
            temp = reader.get(mid)
            if(temp == target):
                return mid
            if(temp > target):
                hi = mid - 1
            else:
                lo = mid + 1
        return -1
        