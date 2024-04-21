# Sort binary tree by level
# Codewars: https://www.codewars.com/kata/52bef5e3588c56132c0003bc/train/python
from collections import deque

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(root):
    if root:
        res = []
        to_go = deque([root])
        while len(to_go) > 0:
            node = to_go.popleft()
            if node is None:
                continue
            res.append(node.value)
            to_go.append(node.left)
            to_go.append(node.right)
        return res
    return []