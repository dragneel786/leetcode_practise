class Solution:
    def checkRecord(self, n: int) -> int:
        # State Transition.
        M = 10 ** 9 + 7
        a0l0 = 1
        a0l1 = a0l2 = a1l0 = a1l1 = a1l2 = 0
        for i in range(n):
            a0l0_ = (a0l1 + a0l2 + a0l0) % M
            a0l2 = a0l1
            a0l1 = a0l0
            a0l0 = a0l0_
            
            a1l0_ = (a0l0 + a1l0 + a1l1 + a1l2) % M 
            a1l2 = a1l1
            a1l1 = a1l0
            a1l0 = a1l0_
        
        return (a0l0 + a0l1 + a0l2 + a1l0 + a1l1 + a1l2) % M
            