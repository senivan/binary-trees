# delete a node in a BST
# leetcode: https://leetcode.com/problems/delete-node-in-a-bst/
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root, key):
        if root:
            if root.val == key:
                if root.left is None:
                    return root.right
                if root.right is None:
                    return root.left
                temp = root.right
                while temp.left:
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right, temp.val)
            elif root.val > key:
                root.left = self.deleteNode(root.left, key)
            else:
                root.right = self.deleteNode(root.right, key)
            return root
        return None
