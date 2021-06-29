class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        dic = {}
        for word in strs:
            s_w = ''.join(sorted(word))
            if s_w in dic:
                dic[s_w].append(word)
            else:
                dic[s_w] = [word]
        res = []
        
        for value in dic.values():
            res.append(value)
        return res