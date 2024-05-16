# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
     
        if not root:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                return None

            if not root.left:
                return root.right
            if not root.right:
                return root.left

            successor = findMinNode(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root

def findMinNode(node):
    while node.left:
        node = node.left
    return node
