from utils.LinkedList import *


class Solution(object):

    def convertToNum(self, head):

        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        ret = 0
        i = 1
        while lst:
            ret += lst.pop(0) * i
            i *= 10

        return ret

    def buildFromNum(self, num):

        curr = None
        head = None
        nsl = list(str(num))

        while nsl:

            digit = nsl.pop()
            node = ListNode(digit)

            if head is None:
                head = node
                curr = node
            else:
                curr.next = node
                curr = curr.next

        return head

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.buildFromNum(self.convertToNum(l1) + self.convertToNum(l2))


def main():

    l1 = LinkedList().buildFromList([5, 6, 4])
    l2 = LinkedList().buildFromList([2, 4, 3])

    ret = Solution().addTwoNumbers(l1.head, l2.head)
    LinkedList.dump(ret)


if __name__ == '__main__':
    main()

