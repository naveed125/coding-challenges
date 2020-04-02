from utils.BinaryTree import *
import sys


class Solution(object):
    def isValidBST(self, root):

        success = True
        if not root:
            return success

        success, _min, _max = self.isValidNode(root)
        return success

    def isValidNode(self, node):

        l_min, l_max, r_min, r_max, = node.val, node.val, node.val, node.val

        if node.left:
            success, l_min, l_max = self.isValidNode(node.left)
            if not success:
                return False, 0, 0

            if l_max >= node.val:
                return False, 0, 0

        if node.right:
            success, r_min, r_max = self.isValidNode(node.right)
            if not success:
                return False, 0, 0

            if r_min <= node.val:
                return False, 0, 0

        _min, _max = min(node.val, l_min), max(node.val, r_max)
        return True, _min, _max


if __name__ == '__main__':

    bt = BinaryTree()
    # print(Solution().isValidBST(bt.fromList([5, 1, 6, None, None, 3, 7])))
    # print(Solution().isValidBST(bt.fromList([1])))
    # print(Solution().isValidBST(bt.fromList([2, 1, 3])))
    # print(Solution().isValidBST(bt.fromList([5, 1, 3])))
    print(Solution().isValidBST(bt.fromList([3,1,5,0,2,4,6])))
