class Solution:
    def countAndSay(self, n: int) -> str:
        if(n == 1):
            return "1"
        
        say_num = self.countAndSay(n - 1) + '-'
        count = 1
        ret = ""
        for i in range(1, len(say_num)):
            if(say_num[i - 1] != say_num[i]):
                ret += (str(count) + say_num[i - 1])
                count = 0
            count += 1
            
        return ret
            