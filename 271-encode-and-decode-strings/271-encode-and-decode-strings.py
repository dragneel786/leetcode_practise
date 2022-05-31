class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        en = []
        for s in strs:
            ordList = list()
            for c in s:
                ordList.append(str(ord(c)))
            en.append(",".join(ordList))
        return "|".join(en)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if(not s):
            return [""]
        
        de = []
        for w in s.split("|"):
            val = ""
            for c in w.split(","):
                if(c):
                    val += (chr(int(c)))
            de.append(val)
            
        return de
                
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))