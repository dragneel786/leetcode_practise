def reverseWords(s: str) -> str:
    s = s[::-1]
    first = 0
    for i in reversed(s.split()):
        if first == 0:
            s = ""
            first += 1
        s += (" " + i)
            
    print(s[1:])
reverseWords("Let's take LeetCode contest")