from exercises import Node, insert_left, insert_right, preorder, is_unival_tree


def test_node():
    tree = Node(1, Node(2), Node(3))
    assert tree.value == 1
    assert tree.left.value == 2
    assert tree.right.value == 3


def test_insert_left():
    tree = Node("A")
    insert_left(tree, "B")
    assert tree.left.value == "B"
    insert_left(tree, "Z")
    assert tree.left.value == "Z"
    assert tree.left.left.value == "B"


def test_insert_right():
    tree = Node("A")
    insert_right(tree, "B")
    assert tree.right.value == "B"
    insert_right(tree, "Z")
    assert tree.right.value == "Z"
    assert tree.right.right.value == "B"


def test_preorder():
    tree = Node("1", Node("2", Node("4"), Node("5")), Node("3", Node("6"), Node("7")))
    assert preorder(tree) == ["1", "2", "4", "5", "3", "6", "7"]


def test_is_unival_tree():
    pass
