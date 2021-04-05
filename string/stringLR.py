class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        st = []
        text = list(s)
        for i in range(len(text)):
            st.append(text[i])
            for j in range(i + 1, len(text)):
                if text[j] != st[len(st) - 1]:
                    st.pop()
                else: st.append(text[j])
                if st == []:
                    res += 1
                    i = j + 1
                    break
        return res        

        stack = []
        counter = 0
        for char in s:
            if stack:
                if stack[-1] == char:
                    stack.append(char)
                elif stack[-1] != char:
                    stack.pop()
                continue
            counter += 1
            stack.append(char)
        return counter    