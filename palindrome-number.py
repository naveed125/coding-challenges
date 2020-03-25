# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# Could you solve it without converting the integer to a string?


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if num < 0:
            return False

        return self.isPalindromeList(list(str(x)))

    def isPalindromeList(self, _list):
        length = len(_list)
        for i in range(int(length / 2)):
            if _list[i] != _list[length - i - 1]:
                return False

        return True


if __name__ == '__main__':

    num = 121
    ret = Solution().isPalindrome(num)
    print("Number {} is Palindrome: {}".format(num, ret))

    stack = []
    temp = num
    while temp > 0:
        digit = temp % 10
        temp = int((temp - digit) / 10)
        stack.append(digit)

    ret = Solution().isPalindromeList(stack)
    print("Number {} is Palindrome: {}".format(num, ret))
