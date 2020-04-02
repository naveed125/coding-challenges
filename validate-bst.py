from utils.BinaryTree import *
import sys


class Solution(object):
    def isValidBST(self, root):

        success = True
        if not root:
            return success

        return self.helper(root)

    def helper(self, node):

        print("checking node", node.val)

        if node.left:
            (success, _max) = self.checkLeft(node.left)
            if not success:
                return False

            if _max >= node.val:
                return False

        if node.right:
            (success, _min) = self.checkRight(node.right)
            if not success:
                return False

            if _min <= node.val:
                return False

        return True

    def checkLeft(self, node):

        print("checking left", node.val)
        _max = None
        if not node.left:
            return True, node.val

        (success, _max) = self.helper(node.left)

        if not success:
            return False, _max

        if node.val <= _max:
            return False, _max

        return True, node.val

    def checkRight(self, node):

        print("checking right", node.val)
        _min = None
        if not node.right:
            return True, node.val

        (success, _min) = self.helper(node.right)

        if not success:
            return False, _min

        if node.val <= _min:
            return False, _min

        return True, node.val


if __name__ == '__main__':

    bt = BinaryTree()
    # print(Solution().isValidBST(bt.fromList([5,1,6,None,None,3,7])))
    # print(Solution().isValidBST(bt.fromList([3, 1, 2])))
    print(Solution().isValidBST(bt.fromList([3,1,5,0,2,4,6])))
