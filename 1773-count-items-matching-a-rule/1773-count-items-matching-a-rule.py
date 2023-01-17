class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        imap = {"type": 0, "color":1, "name":2}
        return len(list(filter(lambda item: item[imap[ruleKey]] == ruleValue, items)))