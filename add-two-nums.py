# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        s1, s2 = [], []

        head = l1
        while head:
            s1.append(head.val)
            head = head.next

        head = l2
        while head:
            s2.append(head.val)
            head = head.next

        count = max(len(s1), len(s2))

        carry = 0
        current = None
        head = None
        for i in range(count):

            lhs = 0
            if len(s1) > 0:
                lhs = s1.pop()

            rhs = 0
            if len(s2) > 0:
                rhs = s2.pop()

            total = lhs + rhs + carry
            if total > 9:
                carry = 1
                total = total % 10
            else:
                carry = 0

            temp = ListNode(total)
            if head is None:
                head = temp

            if current is not None:
                current.next = temp

            current = temp

        if carry > 0:
            current.next = ListNode(1)

        return head


def main():
    h1 = None
    h2 = None

    h1 = build([5, 6, 4])
    h2 = build([2, 4, 3])

    # h1 = build([1, 2])
    # h2 = build([1, 2])

    h1 = build([5])
    h2 = build([5])

    sol = Solution()
    ret = sol.addTwoNumbers(h1, h2)
    dump(ret)


def build(fromList):

    head = None
    prev = None
    for i in fromList:

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

