class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        curr = []
        paras = []
        char_count = 0
        for word in words:
            space_size = len(curr)
            word_size = len(word)
            if (char_count + space_size + word_size > maxWidth):
                space_size -= 1
                remain = (maxWidth - char_count)

                if(not space_size):
                    paras.append(curr[0] + (' ' * remain))

                else:
                    added_space_size = remain // space_size
                    spaces = ' ' * added_space_size
                    remain %= space_size

                    para = ''
                    for c in curr[:-1]:
                        para += c + spaces + (' ' * (remain > 0))
                        remain -= 1

                    para += curr[-1]
                    paras.append(para)

                curr = []
                char_count = 0

            curr.append(word)
            char_count += len(word)
        
        if(curr):
            para = ' '.join(curr)
            para += ' ' * (maxWidth - len(para))
            paras.append(para)
            
        return paras