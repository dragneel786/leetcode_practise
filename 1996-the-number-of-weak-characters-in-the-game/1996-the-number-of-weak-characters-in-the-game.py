class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # [5, 5], [6, 3], [3, 6]
        # [3, 6], [5, 5], [6, 3]
        properties.sort(key = lambda x: [x[0], -x[1]])
        pa, pd = properties[-1]
        weaks = 0
        for ca, cd in properties[:-1][::-1]:
            if(ca < pa and cd < pd):
                weaks += 1
            
            if(cd > pd):
                pa = ca
                pd = cd

        return weaks
        

            