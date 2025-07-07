class Solution:
    def concatHex36(self, n: int) -> str:
        def get_convo(val, base):
            res = []
            while(val):
                rem = val % base
                val //= base
                if rem > 9:
                    res.append(chr(65 + (rem - 10)))
                else:
                    res.append(str(rem))
            
            return ''.join(res)[::-1]

        n2, n3 = n ** 2, n ** 3
        return get_convo(n2, 16) + get_convo(n3, 36)
        # return 