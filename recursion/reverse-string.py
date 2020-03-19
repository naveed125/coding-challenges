class Solution(object):
    def reverseString(self, s, i=0):
        """
        :param i:
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        count = len(s)

        if i >= (count / 2):
            return

        tmp = s[i]
        s[i] = s[count - i - 1]
        s[count - i - 1] = tmp

        self.reverseString(s, i + 1)


def main():

    word = ['H', 'e', 'l', 'l', 'o']

    solution = Solution()
    solution.reverseString(word)

    print(word)


if __name__ == "__main__":
    main()
