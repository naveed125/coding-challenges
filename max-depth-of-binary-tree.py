from utils.BinaryTree import BinaryTree


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: BinaryTreeNode
        :type depth: int
        :rtype: int
        """
        return self.depth(root, 1)

    def depth(self, node, cur):

        if not node:
            return 0

        if not node.left and not node.right:
            return cur

        depthLeft, depthRight = 0, 0
        if node.left:
            depthLeft = self.depth(node.left, cur + 1)

        if node.right:
            depthRight = self.depth(node.right, cur + 1)

        return max(depthRight, depthLeft)


if __name__ == '__main__':
    bt = BinaryTree()
    root = bt.fromList([3, 9, 20, None, None, 15, 7])
    BinaryTree.dump(root)

    print(Solution().maxDepth(root))
