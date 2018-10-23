"""
This module implements the Linked List class
along with its supporting Node class.
"""


class Node:
    """
    The class to represent the Node of the linked list.
    """
    def __init__(self, data: object = None) -> None:
        self._data = data
        self._next = None


class LinkedList:
    """
    The LinkedList class.
    """
    def __init__(self) -> None:
        self._head = Node()
        self._size = 0

    def __repr__(self) -> object:
        current = self._head
        result = "LinkedList(["

        while current._next._next is not None:
            current = current._next
            result += str(current._data) + ", "
        current = current._next

        return result + str(current._data) + ")]"

    def __eq__(self, other) -> bool:
        if type(self) is not type(other):
            return False
        if self.size() != other.size():
            return False

        current = self._head
        other_current = other._head
        while current._next is not None:
            current = current._next
            other_current = other_current._next

            if current._data != other_current._data:
                return False

        return True

    def size(self) -> int:
        """
        Returns the size of the linked list.
        """
        return self._size

    def append(self, data: object) -> None:
        """
        Appends an element to the end of the linked list.
        """
        current = self._head

        while current._next is not None:
            current = current._next

        current._next = Node(data)
        self._size += 1

    def insert(self, data: object, index: int) -> None:
        """
        Inserts the element at the given index.
        """
        if index < 0 or index > self._size - 1:
            raise IndexError("Index out of bounds!")

        if index == self._size - 1:
            self.append(data)
            return

        current = self._head
        tracker = 0

        while tracker < index - 1:
            current = current._next
            tracker += 1

        temp = current._next
        current._next = Node(data)
        current._next._next = temp

        self._size += 1

    def remove(self, index: int) -> None:
        """
        Given the index, removes the element at that index.
        """
        if index < 0 or index > self._size - 1:
            raise IndexError("Index out of bounds!")

        current = self._head
        tracker = 0

        while tracker < index - 1:
            current = current._next
            tracker += 1

        current._next = current._next._next
        self._size -= 1

    def index(self, data: object) -> int:
        """
        Given the value, returns the first index where the
        value occurs. If there is no such value, returns false.
        """
        current = self._head
        tracker = 0

        while current._next is not None:
            current = current._next

            if current._data == data:
                return tracker

            tracker += 1

        return False


def main():
    linked_list = LinkedList()
    for i in range(10):
        linked_list.append(i)

    # Test the 'LinkedList' datatype creation
    if linked_list:
        print("Test 0 passed")
    else:
        print("Test 0 failed")

    # Test the '__repr__' magic method
    if repr(linked_list) == "LinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9)]":
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    other_linked_list = LinkedList()
    for i in range(10):
        other_linked_list.append(i)
    # Test the '__eq__' magic method
    if linked_list == other_linked_list:
        print("Test 2 passed")
    else:
        print("Test 2 failed")

    # Test the 'size' method
    if linked_list.size() == 10:
        print("Test 3 passed")
    else:
        print("Test 3 failed")

    linked_list.insert("Item", 5)

    # Test the 'insert' method
    if repr(linked_list) == "LinkedList([0, 1, 2, 3, Item, 4, 5, 6, 7, 8, 9)]":
        print("Test 4 passed")
    else:
        print("Test 4 failed")

    linked_list.remove(5)

    # Test the 'remove' method
    if repr(linked_list) == "LinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9)]":
        print("Test 5 passed")
    else:
        print("Test 5 failed")

    # Test the 'index' method
    if linked_list.index(5) == 5:
        print("Test 6 passed")
    else:
        print("Test 6 failed")


if __name__ == "__main__":
    main()
