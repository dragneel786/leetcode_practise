class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        def compute(string):
            lcount = []
            string += '-'
            count = 0
            for i in range(len(string)):
                if(i > 0 and\
                   string[i - 1] != string[i]):
                    lcount.append((string[i - 1], count))
                    count = 0

                count += 1
            return lcount
        
        
        for a, b in zip_longest(compute(name), compute(typed)):
            if(not a or not b or \
               a[0] != b[0] or a[1] > b[1]):
                return False
        
        return True