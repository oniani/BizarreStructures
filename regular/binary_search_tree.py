"""
This module implements a binary
search tree data structure.
"""


class TreeNode:
    """
    A class for the binary search tree.
    """
    def __init__(self, data: object = None):
        self._data = data
        self._left = None
        self._right = None

    def __repr__(self) -> object:
        return "TreeNode({}, {}, {})".format(self._data, self._left, self._right)
    
    def get_val(self) -> object:
        return self._data
    
    def set_val(self, data: object) -> None:
        self._data = data
    
    def get_left(self) -> object:
        return self._left
    
    def set_left(self, data : object) -> None:
        self._left = data

    def get_right(self) -> object:
        return self._right

    def set_right(self, data: object) -> None:
        self._right = data

    def traverse(self):
        if self._left is not None:
            for element in self._left:
                yield element
        
        yield self.get_val()

        if self._right is not None:
            for element in self._right:
                yield element


class BinarySearchTree:
    def __init__(self) -> None:
        self._root = None

    def _insert(self, data, current):
        if data < current._data:
            if current._left is None:
                current._left = TreeNode(data)
            else:
                return self._insert(data, current._left)
        elif data > current._data:
            if current._right is None:
                current._right = TreeNode(data)
            else:
                return self._insert(data, current._right)
        else:
            print("The value already exists in the binary search tree!")

    def insert(self, data):
        if self._root is None:
            self._root = TreeNode(data)
        else:
            self._insert(data, self._root)

    def _print_in_order(self, current):
        if current is not None:
            self._print_in_order(current._left)
            print(current._data)
            self._print_in_order(current._right)

    def print_in_order(self):
        if self._root is not None:
            self._print_in_order(self._root)
    
    def _height(self, current: object, tracker: int) -> int:
        if current is None:
            return tracker
        left_height = self._height(current._left, tracker + 1)
        right_height = self._height(current._right, tracker + 1)
        return max(left_height, right_height)

    def height(self) -> int:
        if self._root is None:
            return 0
        return self._height(self._root, 0)
    
    def _search(self, data, current) -> bool:
        if data == current._data:
            return True
        elif data < current._data and current._left is not None:
            return self._search(data, current._left)
        elif data > current._data and current._right is not None:
            return self._search(data, current_right)
        return False

    def search(self, data) -> bool:
        if self._root is None:
            return False
        return self._search(data, self._root)


def main():
    from random import randrange as rng

    bst = BinarySearchTree()
    
    for i in range(100):
        bst.insert(rng(1000))
    
    bst.print_in_order()
    print(bst.height())
    print(bst.search(10))


if __name__ == "__main__":
    main()
