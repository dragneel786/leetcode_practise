class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        def is_valid(state):
            for j in range(1, len(state)):
                if state[j - 1] == state[j]:
                    return False

            return True

        def is_valid_alter(state1, state2):
            for a, b in zip(state1, state2):
                if a == b:
                    return False
            
            return True

        mod = 10**9 + 7
        valid_state = dict()
        for i, state in enumerate(product([0,1,2], repeat=m)):
            if is_valid(state):
                valid_state[i] = state

        compatible_states = defaultdict(list)
        for mask1, state1 in valid_state.items():
            for mask2, state2 in valid_state.items():
                if is_valid_alter(state1, state2):
                    compatible_states[mask1].append(mask2)

        
        dp = {k: 1 for k in valid_state.keys()}
        for _ in range(1, n):
            new_dp = Counter()
            for key in dp.keys():
                for next_state in compatible_states[key]:
                    new_dp[next_state] += dp[key]
                    new_dp[next_state] %= mod
            
            dp = new_dp
            
        return sum(dp.values()) % mod
     
