#Given a string s, find the length of the longest substring without repeating characters.
#
# abcabcbb
# bbbbbb
# pwwkew
# kalbkaleq

def lengthOfLongestSubstring(s):
        pointer=0
        seenChars=set()
        maxlength=0
        curmax=0
        while pointer<=len(s)-1:
            for j in s[pointer:]:
                if j not in seenChars:
                    seenChars.add(j)
                    curmax+=1
                    maxlength=max(curmax, maxlength)
                else:
                    pointer+=1
                    seenChars.clear()
                    maxlength=max(curmax, maxlength)
                    curmax=0
                    break
                maxlength=max(curmax,maxlength)
        return maxlength
        
print(lengthOfLongestSubstring('kalooga'))
