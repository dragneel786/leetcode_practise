class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        po = -1
        st = deque()
        first = False
        ans = 0
        for b in s:
            if(b == "("):
                st.append(b)
                po += 1
                first = True
            else:
                if(first):
                    ans += 2 ** po
                    first = False
                po -= 1
                st.pop()

        return ans