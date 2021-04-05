class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        def getSum(n):
            if n < 10:
                return n
            else: 
                return getSum(n//10) + getSum(n % 10)
        def getProd(n):
            if n < 10:
                return n
            else:
                return getProd(n//10) * getProd(n % 10)
        return getProd(n) - getSum(n)