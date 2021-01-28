class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        # 如果n 是奇数，需要在多乘一个x   x^5 = x^2 * x^2 * x 
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)



class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0.0: return 0.0
        res = 1
        if n < 0: x, n = 1 / x, -n
        while n:
            if n & 1: res *= x
            x *= x
            n >>= 1
        return res

