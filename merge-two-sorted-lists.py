from utils.LinkedList import *


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:
            return l2

        if not l2:
            return l1

        head = None
        if l1.val < l2.val:
            head = l1
        else:
            head = l2

        ll = LinkedList()

        while True:
            if not l1 and not l2:
                break

            if not l1:
                ll.append(l2.val)
                l2 = l2.next
                continue

            if not l2:
                ll.append(l1.val)
                l1 = l1.next
                continue

            if l1.val < l2.val:
                ll.append(l1.val)
                l1 = l1.next
            else:
                ll.append(l2.val)
                l2 = l2.next

        return ll.head


if __name__ == '__main__':

    list1 = LinkedList.buildFromList([1, 3, 5])
    list2 = LinkedList.buildFromList([])

    # LinkedList.dump(list1)
    # LinkedList.dump(list2)

    ret = Solution().mergeTwoLists(list1, list2)
    LinkedList.dump(ret)
