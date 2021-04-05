class Solution:
    def isHappy(self, n: int) -> bool:
        visitedNums = set()
        while n not in visitedNums:
            visitedNums.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False

    def sumOfSquares(self, num: int) -> int:
        digit = 0
        output = 0
        while num:
            digit = num % 10
            digit = digit ** 2
            output += digit
            num = num // 10
        return output

print(Solution().isHappy(19))