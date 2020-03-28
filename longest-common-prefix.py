import sys


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) < 1:
            return ""

        first = strs.pop()
        if not strs or len(first) == 0:
            return first

        i = 0
        prev = ""
        while True:

            i += 1
            cur = first[:i]
            for s in strs:
                if i > len(s) or cur != s[:i]:
                    return prev

            prev = cur


if __name__ == '__main__':
    print(Solution().longestCommonPrefix([
        sys.argv[1],
        sys.argv[3],
    ]))
