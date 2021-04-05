class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        def getKey(ruleKey):
            if ruleKey == 'type':
                return 0
            if ruleKey == 'color':
                return 1
            if ruleKey == 'value':
                return 2
            return -1
        itemsNum = 0
        k = getKey(ruleKey)
        for i in items:
            if i[k] == ruleValue:
                itemsNum += 1
        return itemsNum