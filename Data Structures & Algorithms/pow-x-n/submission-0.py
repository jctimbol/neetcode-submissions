class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            res = 1
            for i in range(0, (-1 * n)):
                res /= x
            return res
        elif n == 0:
            return 1
        else:
            res = 1
            for i in range(0, n):
                res *= x
            return res