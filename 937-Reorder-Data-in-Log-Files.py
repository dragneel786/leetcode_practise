class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            splits = log.split(" ")
            idn, content = splits[0], splits[1:]

            if any([c.isalpha() for c in content]):
                letter_logs.append((" ".join(content), idn))
            else:
                digit_logs.append(log)
        
        letter_logs.sort()
        return [f'{idn} {content}' for content, idn in letter_logs]\
         + digit_logs