import sys


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) < 2:
            return len(s)

        i, j = 0, 0
        dict = {}
        _max = 0
        best = 0
        while j < len(s):

            _next = s[j]

#            print("i:{}, j:{}, next:{}".format(i, j, _next))

            if dict.get(_next):
                # print("best: ", s[i:j])
                best = max(best, len(s[i:j]))
                i = i + 1
                j = i
                dict = {}
            else:
                # print("so far so good:", s[i:j+1])
                dict[_next] = 1
                j += 1

        return max(best, len(s[i:j+1]))


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(sys.argv[1]))
