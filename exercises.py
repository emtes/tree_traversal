class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def insert_left(node, value):
    to_insert = Node(value)
    if node.left:
        to_insert.left = node.left
        node.left = to_insert
    else:
        node.left = to_insert


def insert_right(node, value):
    to_insert = Node(value)
    if node.right:
        to_insert.right = node.right
        node.right = to_insert
    else:
        node.right = to_insert


def preorder(node):  # nlr
    list = []
    if node:
        list.append(node.value)
        preorder(node.left)
        preorder(node.right)


def is_unival_tree():
    pass
