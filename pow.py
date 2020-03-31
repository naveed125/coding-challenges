import sys


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        n = min(max(n, -2147483648), 2147483647)

        print("x is ", x)
        print("n is ", n)

        neg = (n < 0)
        n = abs(n)

        y = x
        i = 0
        while i < (n - 1):
            y *= x
            i += 1

        if neg:
            return 1/y
        else:
            return y


if __name__ == '__main__':
    print(Solution().myPow(float(sys.argv[1]), int(sys.argv[2])))
