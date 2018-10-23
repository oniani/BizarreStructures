"""
This module implements a binary
search tree data structure.
"""


class Node:
    """
    Node class for the BinarySearchTree class
    """
    def __init__(self, data: object = None) -> None:
        self._data = data
        self._left = None
        self._right = None

    def get_val(self) -> None:
        return self._data

    def get_left(self) -> object:
        return self._left

    def get_right(self) -> object:
        return self._right

    def set_val(self, data) -> None:
        self._data = data

    def set_left(self, data) -> None:
        self._left = data

    def set_right(self, data) -> None:
        self._right = data
    

class BinarySearchTree:
    """
    The BinarySearchTree class
    """
    def __init__(self, root: object = None) -> None:
        self._root = Node(root)
    
    def insert(self, data: object) -> None:
        if self._root = Node(None):
            self._root = Node(data)
        
        elif data < self._root.get_val():
            self._data.set_left(data)
        
        elif data > self._root.get_val():
            self._data.set_right(data)
