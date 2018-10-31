"""
This module implements the Linked List class
along with its supporting ListNode class.
"""


class ListNode:
    """
    The class to represent the Node of the linked list.
    """
    def __init__(self, data: object = None) -> None:
        self._data = data
        self._next = None

    def __repr__(self) -> object:
        return "ListNode([{}, {}])".format(self._data, self._next)


class LinkedList:
    """
    The LinkedList class.
    """
    def __init__(self) -> None:
        self._head = ListNode()
        self._size = 0

    def __repr__(self) -> object:
        if self._size == 0:
            return "LinkedList([])"

        current = self._head
        result = "LinkedList(["

        while current._next._next is not None:
            current = current._next
            result += repr(current._data) + ", "
        current = current._next

        return result + repr(current._data) + ")]"

    def __eq__(self, other) -> bool:
        if type(self) is not type(other):
            return False
        if len(self) != len(other):
            return False

        current = self._head
        other_current = other._head
        while current._next is not None:
            current = current._next
            other_current = other_current._next

            if current._data != other_current._data:
                return False

        return True

    def __len__(self) -> int:
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

        current._next = ListNode(data)
        self._size += 1

    def insert(self, data: object, index: int) -> None:
        """
        Inserts the element at the given index.
        """
        if index > self._size - 1:
            self.append(data)
        else:
            current = self._head

            for _ in range(index):
                current = current._next

            new_node = ListNode(data)
            new_node._next = current._next
            current._next = new_node

            self._size += 1

    def remove(self, index: int) -> None:
        """
        Given the index, removes the element at that index.
        """
        if index < 0 or index > self._size - 1:
            raise IndexError("Index out of bounds!")

        current = self._head
        tracker = 0

        while tracker < index:
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

    def empty(self):
        """
        Empty the linked list.
        """
        self._head._next = None
        self._size = 0

    def is_empty(self):
        """
        Check the emptiness of the linked list.
        """
        return self._head._next is None and self._size == 0


def main():
    # Test the 'LinkedList' datatype creation
    linked_list = LinkedList()

    if not linked_list:
        print("Test 0 passed")
    else:
        print("Test 0 failed")

    # Test the '__repr__' magic method
    for i in range(10):
        linked_list.append(i)

    if repr(linked_list) == "LinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9)]":
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    # Test the '__eq__' magic method
    other_linked_list = LinkedList()
    for i in range(10):
        other_linked_list.append(i)

    if linked_list == other_linked_list:
        print("Test 2 passed")
    else:
        print("Test 2 failed")

    # Test the 'size' method
    if len(linked_list) == 10:
        print("Test 3 passed")
    else:
        print("Test 3 failed")

    # Test the 'insert' method
    linked_list.insert("X", 5)

    if repr(linked_list) == "LinkedList([0, 1, 2, 3, 4, 'X', 5, 6, 7, 8, 9)]":
        print("Test 4 passed")
    else:
        print("Test 4 failed")

    # Test the 'remove' method
    linked_list.remove(5)

    if repr(linked_list) == "LinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8, 9)]":
        print("Test 5 passed")
    else:
        print("Test 5 failed")

    # Test the 'index' method
    if linked_list.index(5) == 5:
        print("Test 6 passed")
    else:
        print("Test 6 failed")

    # Test the 'empty' method
    linked_list.empty()

    if linked_list == LinkedList():
        print("Test 7 passed")
    else:
        print(linked_list)
        print("Test 7 failed")

    # Test the 'is_empty' method
    if linked_list.is_empty() is True:
        print("Test 8 passed")
    else:
        print("Test 8 failed")


if __name__ == "__main__":
    main()
