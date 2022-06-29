class Fn:
    def __init__(self, id, op, ts):
        self.id = int(id)
        self.op = op
        self.ts = int(ts)
        
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        st = deque()
        for l in logs:
            fn = Fn(*l.split(":"))
            if(fn.op == "start"):
                if(st):
                    top = st[-1]
                    res[top.id] += (fn.ts - top.ts)
                st.append(fn)
            else:
                top = st.pop()
                res[top.id] += (fn.ts - top.ts + 1)
                if(st):
                    st[-1].ts = fn.ts + 1
        return res
        