# Binary tree traversal
# Codewars: https://www.codewars.com/kata/5268956c10342831a8000135/train/python

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def pre_order(root):
    res = []
    if root:
        res.append(root.data)
        temp = pre_order(root.left)
        if temp:
            res.extend(temp)
        
        temp = pre_order(root.right)
        if temp:
            res.extend(temp)
        
        return res
    return []

def in_order(root):
    res = []
    if root:
        temp = in_order(root.left)
        if temp:
            res.extend(temp)

        res.append(root.data)

        temp = in_order(root.right)
        if temp:
            res.extend(temp)
        
        return res
    return []

def post_order(root):
    res = []
    if root:
        temp = post_order(root.left)
        if temp:
            res.extend(temp)

        temp = post_order(root.right)
        if temp:
            res.extend(temp)
        
        res.append(root.data)
        
        return res
    return []