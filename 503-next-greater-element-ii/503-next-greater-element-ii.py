class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        st = deque()
        i = 0
        seen = set()
        while(True):
            if(len(st) and i == st[-1]):
                break

            while(len(st) and nums[st[-1]] < nums[i]):
                res[st.pop()] = nums[i]

            if(i not in seen):
                st.append(i)
                seen.add(i)
            i = (i + 1) % n

        while(len(st)):
            res[st.pop()] = -1

        return res