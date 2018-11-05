"""
This module implements a binary search tree data structure.
"""


class TreeNode:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self._data = data
        self._left = left
        self._right = right
        self._parent = parent

    def children(self):
        if self._left is self._right is None:
            return 0
        if self._left or self._right is None:
            return 1
        return 2


class BinarySearchTree:
    def __init__(self, root=None):
        self._root = root

    def _insert(self, data, current):
        if data < current._data:
            if current._left is None:
                current._left = TreeNode(data)
                current._left._parent = current
                return True
            return self._insert(data, current._left)

        elif data > current._data:
            if current._right is None:
                current._right = TreeNode(data)
                current._right._parent = current
                current = current._right
                return True
            return self._insert(data, current._right)

        raise ValueError("Such node is present in the tree!")

    def insert(self, data):
        if self._root is None:
            self._root = TreeNode(data)
        else:
            self._insert(data, self._root)

    def _print_in_order(self, current):
        if current._left is not None:
            self._print_in_order(current._left)
        print(current._data)
        if current._right is not None:
            self._print_in_order(current._right)

    def print_in_order(self):
        """
        This is an iterative solution:
        NOTE: Import a deque object for the faster pop operations.

        def print_in_order(self):
            current = self._root
            while current._left is not None:
                current = current._left
            queue = [current]
            visited = set()
            while queue:
                node = queue.pop(-1)
                if node not in visited:
                    print("The current node is:", node._data)
                    visited.add(node)
                    neighbors = [node._parent, node._right, node._left]
                    for neighbor in neighbors:
                        if neighbor is not None:
                            queue.append(neighbor)
            return visited
        """
        if self._root is not None:
            self._print_in_order(self._root)
        else:
            raise Exception("Empty binary search tree!")

    def pre_order_DFS(self):
        """
        This is a simple application
        of depth first search to do
        a pre-order traversal.

        NOTE: Import the deque object from collections
        for a faster 'pop's. You can do both deque.popleft()
        and deque.pop in O(1).
        """
        visited = set()
        queue = [self._root]
        while queue:
            node = queue.pop(-1)
            if node not in visited:
                print("The current node is:", node._data)
                visited.add(node)
                neighbors = [node._right, node._left]
                for neighbor in neighbors:
                    if neighbor is not None:
                        queue.append(neighbor)

        return visited

    def _height(self, current, height):
        if current is None:
            return height

        left_height = self._height(current._left, height + 1)
        right_height = self._height(current._right, height + 1)

        return max(left_height, right_height)

    def height(self):
        if self._root is None:
            return 0
        else:
            return self._height(self._root, 0) - 1

    def _delete(self, data, current):
        if data < current._data:
            self._delete(data, current._left)

        if data > current._data:
            self._delete(data, current._right)

        if data == current._data:
            if current.children() == 0:
                if current._parent._left is not None:
                    current._parent._left = None
                else:
                    current._parent._right = None

            elif current.children() == 1:
                if current._left is not None:
                    current._parent = current._left
                else:
                    current._parent = current._right

            elif current.children() == 2:
                cursor = current._right
                while cursor._left is not None:
                    cursor = cursor._left
                current._data = cursor._data
                cursor._parent._left = None

            return True

        return False

    def delete(self, data):
        if self._root is None:
            raise Exception("Empty binary search tree!")
        else:
            self._delete(data, self._root)

    def _contains(self, data, current):
        if data < current._data:
            return self._contains(data, current._left)
        if data > current._data:
            return self._contains(data, current._right)
        if data == current._data:
            return True

        return False

    def contains(self, data):
        if self._root is None:
            return -1
        else:
            return self._contains(data, self._root)


def main():
    binary_search_tree = BinarySearchTree()

    # Test the 'BinarySearchTree' datatype creation
    if binary_search_tree:
        print("Test 0 passed")
    else:
        print("Test 0 failed")

    # Test the 'insert' and 'height' methods
    for i in [50, 30, 20, 40, 70, 60, 80]:
        binary_search_tree.insert(i)

    if binary_search_tree.height() == 2:
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    # Test the 'delete' method
    binary_search_tree.delete(20)
    binary_search_tree.delete(40)
    binary_search_tree.delete(60)
    binary_search_tree.delete(80)

    if binary_search_tree.height() == 1:
        print("Test 2 passed")
    else:
        print("Test 2 failed")

    # Test the 'contains' method
    if binary_search_tree.contains(70) is True:
        print("Test 3 passed")
    else:
        print("Test 3 failed")


if __name__ == "__main__":
    main()
