import sys
import re


class Solution:

    def myAtoi(self, s):

        s = s.strip()

        ret = ""
        if s[0:1] == "+":
            s = s[1:]
        elif s[0:1] == "-":
            ret = "-"
            s = s[1:]

        if re.sub("[0-9]", "", s[0:1]) != "":
            return 0

        if not s:
            return 0

        for i in list(s):
            if i in list("0123456789"):
                ret += i
            else:
                break

        return min(max(int(ret), -2147483648), 2147483647)


if __name__ == '__main__':
    # print(Solution().myAtoi(sys.argv[1]))
    print(Solution().myAtoi("-"))
