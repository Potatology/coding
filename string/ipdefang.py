class Solution:
    def defangIPaddr(self, address: str) -> str:
        da = ''
        for i in address:
            if i == '.':
                da = da + ('[.]')
            else:
                da = da + i
        return da

    def defangIPaddr2(self, address: str) -> str:
        ans = []
        for ch in address:
            if ch.isdigit():
                ans.append(ch)
            else:
                ans.append("[.]")
        print(ans)
        return "".join(ans)
    
print(Solution().defangIPaddr2('1.1.1.1'))
    
        