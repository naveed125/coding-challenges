class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None
        self.cur = None

    def append(self, x):

        node = ListNode(x)

        if not self.head:
            self.head = node
            self.cur = node
        else:
            self.cur.next = node
            self.cur = node

    @staticmethod
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

    @staticmethod
    def dump(head):
        while head is not None:
            print(head.val)
            head = head.next

