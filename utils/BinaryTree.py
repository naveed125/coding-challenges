class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree(object):

    #
    # Init the tree
    #
    def __init__(self):
        self.root = None

    #
    # Build a tree from a list recursively
    #
    def fromList(self, _list, index=0):

        if index >= len(_list) or _list[index] is None:
            return None

        # print("index:{}, val:{}".format(index, _list[index]))

        node = BinaryTreeNode(_list[index])
        if index == 0:
            self.root = node

        if index < len(_list):
            node.left = self.fromList(_list, index * 2 + 1)
            node.right = self.fromList(_list, index * 2 + 2)

        return node

    #
    # Dump the tree on screen
    #
    @staticmethod
    def dump(cur=None):

        if cur is None:
            return

        print(cur.val)
        BinaryTree.dump(cur.left)
        BinaryTree.dump(cur.right)
