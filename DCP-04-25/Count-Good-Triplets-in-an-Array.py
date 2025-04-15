class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        def bin_search(val):
            nonlocal n
            low = 0
            high = n
            while(low < high):
                mid = low + ((high - low) // 2)
                if items[mid][0] <= val:
                    low = mid + 1
                else:
                    high = mid
            
            if low == 0:
                return 0
            
            return max_beauty[low - 1]

        n = len(items)
        items.sort(key=lambda x: x[0])
        max_beauty = [0] * n
        max_beauty[0] = items[0][1]
        for i in range(1, n):
            _, b = items[i]
            max_beauty[i] = max(max_beauty[i - 1], b)

        print(max_beauty)
        res = []
        for q in queries:
            res.append(bin_search(q))


        return res

