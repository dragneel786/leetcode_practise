class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = deque()
        for i, p in enumerate(prices):
            while(st and st[-1][0] >= p):
                value, idx = st.pop()
                prices[idx] = value - p
            
            st.append((p, i))
        
        while(st):
            value, idx = st.pop()
            prices[idx] = value
        
        return prices
            