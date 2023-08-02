class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        dire = -1 if (time // (n - 1)) % 2 else 1
        time = time % (n - 1)
        # print(dire, time)
        return (n if(dire < 0) else 1) + (dire * time)
        