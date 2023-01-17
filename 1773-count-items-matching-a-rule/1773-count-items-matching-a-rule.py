class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        imap = {"type": 0, "color":1, "name":2}
        return sum([item[imap[ruleKey]] == ruleValue for item in items])