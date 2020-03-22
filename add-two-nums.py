# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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

    h1 = buildFromList([5, 6, 4])
    h2 = buildFromList([2, 4, 3])

    sol = Solution()
    ret = sol.addTwoNumbers(h1, h2)
    dump(ret)


def buildFromList(lst):

    head = None
    prev = None
    for i in lst:

        new = ListNode(i)

        if head is None:
            head = new

        if prev is None:
            prev = new
        else:
            prev.next = new
            prev = new

    return head


def dump(head):
    while head is not None:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    main()

