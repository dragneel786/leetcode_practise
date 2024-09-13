class Solution:
    def decodeString(self, s: str) -> str:
        
        def dec_str(string):
            if '[' not in string:
                return string

            val = index = 0
            st = []
            while(index < len(string)):
                c = string[index]
                if c.isdigit():
                    val = (val * 10) + int(c)

                elif c.isalpha():
                    st.append(c)

                elif c == '[':
                    op = 1
                    end = index + 1
                    while(op != 0):
                        if string[end] == '[':
                            op += 1

                        elif string[end] == ']':
                            op -= 1

                        end += 1

                    ret = dec_str(string[index + 1: end - 1])
                    st.append(val * ret)
                    index = end - 1
                    val = 0

                index += 1

            return ''.join(st)

        return dec_str(s)
                        
                        
                