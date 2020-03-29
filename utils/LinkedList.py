class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList(object):
    #
    # Create a new empty linked list
    #
    def __init__(self):
        self.head = None
        self.cur = None

    #
    # Append a node to the linked
    #
    def append(self, x):

        node = ListNode(x)

        if not self.head:
            self.head = node
            self.cur = node
        else:
            save = self.cur.next
            self.cur.next = node
            self.cur = node
            self.cur.next = save

    #
    # Build a linked list from a list (iterable)
    #
    def buildFromList(self, lst):

        for i in lst:
            self.append(i)

        return self

    #
    # Dumps the data on screen
    #
    @staticmethod
    def dump(target):

        cur = target
        while cur is not None:
            print(cur.val)
            cur = cur.next

