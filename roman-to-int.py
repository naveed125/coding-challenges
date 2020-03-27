import sys


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        _len = len(s)

        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        specials = {
            'I': ['V', 'X'],
            'X': ['L', 'C'],
            'C': ['D', 'M']
        }

        total = 0
        skip = False
        for i in range(_len):

            if skip:
                skip = False
                continue

            if not dict.get(s[i]):
                raise Exception("Yo what is this")

            cur = 0
            if specials.get(s[i]) and (i < _len - 1):
                _next = s[i+1]
                if _next in specials.get(s[i]):
                    cur = dict.get(_next) - dict.get(s[i])
                    skip = True

            if cur == 0:
                cur = dict.get(s[i])

            total += cur

        return total


if __name__ == '__main__':
    print(Solution().romanToInt(sys.argv[1]))