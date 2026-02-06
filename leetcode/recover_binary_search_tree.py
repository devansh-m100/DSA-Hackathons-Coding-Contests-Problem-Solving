"""
leetcode:
  id: 99
algoexpert:
  title: Repair BST
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
## O(n) time | O(h) space - where n is the number of nodes in the tree 
## and h is the height of the tree
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.node_one = self.node_two = self.previous_node = None
        def inorder_traversal(node):
            # nonlocal node_one, node_two, previous_node
            if node is None:
                return
            inorder_traversal(node.left)
            if self.previous_node is not None and self.previous_node.val > node.val:
                if self.node_one is None:
                    self.node_one = self.previous_node
                self.node_two = node
            self.previous_node = node
            inorder_traversal(node.right)
        inorder_traversal(root)
        self.node_one.val, self.node_two.val = self.node_two.val, self.node_one.val
