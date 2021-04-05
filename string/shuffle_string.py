class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dc = {}
        sl = list(s)
        for i in range(len(s)):
            dc[indices[i]] = sl[i]
        res = ''
        for key in sorted(dc.keys()):
            res += dc[key]
        return res

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ['']*len(indices)
        for index, char in enumerate(s):
            res[indices[index]] = char
        return ''.join(res)