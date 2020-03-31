import sys


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x**n
    

if __name__ == '__main__':
    print(Solution().myPow(float(sys.argv[1]), int(sys.argv[2])))
