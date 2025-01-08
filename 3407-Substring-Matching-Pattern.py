class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        arr = p.split('*')
        if arr[0] == '' or arr[1] == '':
            return arr[0] in s and arr[1] in s
        if arr[0] + arr[1] in s: return True
        l, r = s.find(arr[0]), s.rfind(arr[1])
        if l == -1 or r == -1: return False
        return l+(len(arr[0]))-1 < r