from dataclasses import dataclass


def read_input():
    items = [int(x) for x in input().split()]
    return items


@dataclass
class Node:
    value: int
    parent: any
    left: any = None
    right: any = None


def add(root: Node, key: int) -> None:
    if key == root.value:
        return
    if key < root.value:
        if root.left is None:
            root.left = Node(value=key, parent=root)
        else:
            add(root.left, key)
    if key > root.value:
        if root.right is None:
            root.right = Node(value=key, parent=root)
        else:
            add(root.right, key)


def traverse_recursive_two_childs(root: Node) -> None:
    if root.left is not None:
        traverse_recursive_two_childs(root.left)
    if root.left is not None and root.right is not None:
        print(root.value)
    if root.right is not None:
        traverse_recursive_two_childs(root.right)


def traverse_two_childs(items: list):
    root = Node(value=items[0], parent=None)
    for item in items:
        if item == 0:
            break
        add(root, item)
    traverse_recursive_two_childs(root)


def main():
    traverse_two_childs(read_input())


if __name__ == '__main__':
    main()
