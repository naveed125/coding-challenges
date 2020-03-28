import sys


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        dict = {
            '{': '}',
            '[': ']',
            '(': ')'
        }

        stack = []
        for i in range(len(s)):
            if s[i] in dict.keys():
                stack.append(s[i])
            elif s[i] in dict.values():
                if not stack or dict.get(stack.pop(len(stack) - 1)) != s[i]:
                    return False
            else:
                raise Exception("Invalid char:{}".format(s[i]))

        return len(stack) == 0


if __name__ == '__main__':
    print(Solution().isValid(
        sys.argv[1]
    ))
