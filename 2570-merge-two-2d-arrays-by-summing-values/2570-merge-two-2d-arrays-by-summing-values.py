class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        res = []
        n1, n2 = len(nums1), len(nums2)
        i = j = 0
        while(i < n1 or j < n2):
            # print(i, n1, j, n2)
            if(j >= n2 or (i < n1 and nums1[i][0] < nums2[j][0])):
                res.append(nums1[i])
                i += 1
            
            elif(i >= n1 or (j < n2 and nums1[i][0] > nums2[j][0])):
                res.append(nums2[j])
                j += 1
            
            else:
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
        
        return res
        