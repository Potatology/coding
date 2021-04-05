class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jd = {i:0 for i in jewels}
        for i in range(len(jewels)):
            if jewels[i] in stones:
                for s in stones:
                    if jewels[i] == s:
                        jd[jewels[i]] += 1
        jwl = 0
        for v in jd.values():
            jwl += v
        return jwl

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in jewels:
            for j in stones:
                if i == j:
                    count += 1
        return count