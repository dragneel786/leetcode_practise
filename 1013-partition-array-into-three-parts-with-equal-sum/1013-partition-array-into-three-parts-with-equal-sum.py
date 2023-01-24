class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)
        imap = defaultdict(list)
        imap[arr[0]].append(0)
        for i in range(1, n):
            arr[i] += arr[i - 1]
            imap[arr[i]].append(i)
        
        for i in range(n - 2):
            for idx in imap[(arr[-1] - arr[i])]:
                if(i < idx < n - 1 and arr[i] == (arr[idx] - arr[i])):
                    return True
        
        return False
                