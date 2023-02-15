class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        carry = 0
        for i in range(n - 1, -1, -1):
            carry += (k % 10) + num[i]
            num[i] = carry % 10
            carry //= 10
            k //= 10
            
            if(carry == k == 0):
                return num
        
        front = []
        while(k):
            carry += (k % 10)
            front.append(carry % 10)
            carry //= 10
            k //= 10
            if(k == 0):
                front.reverse()
                num = front + num
            
        return [carry] + num if(carry) else num
            