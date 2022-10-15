class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        def include(curr_idx, prev_char,\
                freq_count, remain_k):
        
            if(prev_char == s[curr_idx]):
                val = get_min_len(curr_idx + 1, prev_char,\
                                    freq_count + 1, remain_k)

                if(freq_count == 1 or\
                   freq_count == 9 or\
                   freq_count == 99):
                    return val + 1

                return val

            val = get_min_len(curr_idx + 1, s[curr_idx],\
                1, remain_k)

            return val + 1


        def get_min_len(curr_idx, prev_char,\
                        freq_count, remain_k):
            nonlocal n
            if(remain_k < 0):
                return inf

            if(curr_idx == n):
                return 0

            key = (curr_idx, prev_char,\
                    freq_count, remain_k)

            if(key in memo):
                return memo[key]

            #Exclude
            ret = get_min_len(curr_idx + 1, prev_char,\
                                freq_count, remain_k - 1)

            #Include
            ret = min(ret, include(curr_idx, prev_char,\
                                    freq_count, remain_k))

            memo[key] = ret
            return ret


        n = len(s)
        memo = {}
        return get_min_len(0, '#', 0, k)
