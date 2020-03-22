import sys


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            reverse_x = int(str(x)[::-1])
            if reverse_x & 0x7fffffff == reverse_x:
                return reverse_x
            else:
                return 0
        elif x < 0:
            reverse_x = -int(str(abs(x))[::-1])
            if reverse_x & -0x80000000 == -0x80000000:
                return reverse_x
            else:
                return 0
        else:
            return 0


if __name__ == '__main__':
    sol = Solution()
    ret = sol.reverse(int(sys.argv[1]))
    print(ret)
