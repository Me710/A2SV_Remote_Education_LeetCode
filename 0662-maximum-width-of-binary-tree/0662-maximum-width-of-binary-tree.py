# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = deque([(root, 0)])  
        max_width = 1

        while queue:
            level_length = len(queue)
            level_start = queue[0][1]  

            for _ in range(level_length):
                node, index = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))

            max_width = max(max_width, index - level_start + 1)

        return max_width
