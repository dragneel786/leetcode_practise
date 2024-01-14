class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        
        def get_k_digit(values):
            def nxt_perm(num: list) -> list:
                i = n - 1
                while i > 0 and num[i-1] >= num[i]:
                    i -= 1
                j = i
                while j < n and num[i-1] < num[j]:
                    j += 1
                num[i-1], num[j-1] = num[j-1], num[i-1]
                num[i:] = num[i:][::-1] 
                return num
            
            n = len(values)
            for _ in range(k):
                perm = nxt_perm(values)
                values = perm

            return values


        def count_swaps(nums1, nums2):
            n = len(nums1)
            total_swaps = 0
            for i in range(n):
                if(nums1[i] != nums2[i]):
                    for s in range(i, n):
                        if(nums1[i] == nums2[s]):
                            break
                    
                    for j in range(s, i, -1):
                        nums2[j], nums2[j - 1] = \
                            nums2[j - 1], nums2[j]
                        total_swaps += 1
            
            return total_swaps
                
                       
        wonderful_k = get_k_digit(list(map(int, list(num))))
        num = list(map(int, list(num)))
        return count_swaps(wonderful_k, num)
        
        
            