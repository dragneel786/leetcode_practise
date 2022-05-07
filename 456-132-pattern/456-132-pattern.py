class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st = deque()
        second = -math.inf
        for n in reversed(nums):
            if(n < second):
                return True
            while(len(st) and st[-1] < n):
                second = st.pop()
            st.append(n)
        return False
                