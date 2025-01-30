class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        MAX = 1001
        prefix_arr = [0] * MAX
        for cap, frm, to in trips:
            prefix_arr[frm] += cap
            prefix_arr[to] -= cap

        for i in range(MAX):
            capacity -= prefix_arr[i]
            if capacity < 0:
                return False
        
        return True