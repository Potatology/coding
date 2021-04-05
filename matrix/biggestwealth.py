class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        [[1,2,3],
         [3,2,5],
         [4,1,2]]
        
        maxW = 0
        sums = []
        g = (sum(row) for row in accounts)
        for i in range(len(accounts)):
            cw = next(g)
            sums.append(cw)
            maxW = max(maxW, cw)
        return maxW
        
        
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxw = 0
        for acc in accounts:
            sumw = 0
            for record in acc:
                sumw += record
            maxw = max(maxw, sumw)
        return maxw