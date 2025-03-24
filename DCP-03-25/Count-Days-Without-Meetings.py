class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        ans = meetings[0][0] - 1
        curr = meetings[0][1]
        for start, end in meetings[1:]:
            ans += max(0, start - curr - 1)
            # print(curr, start)
            curr = max(end, curr)
            # print("after", end)

        ans += (days - curr)
        return ans