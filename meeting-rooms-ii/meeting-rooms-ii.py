class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        size = max(map(max, intervals)) + 1
        index_arr = [0] * size
        for (s, e) in intervals:
            index_arr[s] += 1
            index_arr[e] -= 1
        
        val = maxv = 0
        for i in range(1, size):
            val += index_arr[i - 1]
            maxv = max(maxv, val)
    
        return maxv