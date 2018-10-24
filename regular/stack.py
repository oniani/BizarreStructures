"""
This class implements the stack datatype
using a simple built-in Python list datatype
"""


class Stack:
    def __init__(self, data: list = []) -> None:
        self._data = data

    def __repr__(self) -> object:
        result = "Stack(["

        for i in range(len(self._data)):
            if i < len(self._data) - 1:
                result += str(self._data[i]) + ", "
            else:
                result += str(self._data[i]) + "])"

        return result

    def __eq__(self, other) -> bool:
        if type(self) is not type(other):
            return False
        if self.size() != other.size():
            return False
        for i in range(len(self._data)):
            if self._data[i] != other._data[i]:
                return False
        return True

    def size(self) -> int:
        """
        Returns the size of the stack.
        """
        return len(self._data)

    def push(self, data: object) -> None:
        """
        Pushes the value to the stack.
        """
        self._data.append(data)

    def top(self, data: object) -> None:
        """
        Returns the top value of the stack.
        """
        return self._data[-1]

    def pop(self) -> object:
        """
        Remove the last item from the stack and
        return it in the end.
        """
        if self.size() == 0:
            raise IndexError("Cannot pop the empty stack!")

        data = self._data[-1]
        self._data = self._data[:-1]
        return data

    def clear(self) -> object:
        """
        Remove all the items from the stack.
        """
        self._data = []

    def is_empty(self) -> bool:
        """
        Returns true if the stack is empty
        and false otherwise
        """
        return self._data == []


def main():
    stack = Stack([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Test the 'Stack' datatype creation
    if stack:
        print("Test 0 passed")
    else:
        print("Test 0 failed")

    # Test the '__repr__' magic method
    if str(stack) == "Stack([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])":
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    # Test the '__eq__' magic method
    other_stack = Stack([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    if stack == other_stack:
        print("Test 2 passed")
    else:
        print("Test 2 failed")

    # Test the 'size' method
    if stack.size() == 10:
        print("Test 3 passed")
    else:
        print("Test 3 failed")

    stack.push(10)

    # Test the 'push' method
    if str(stack) == "Stack([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])":
        print("Test 4 passed")
    else:
        print("Test 4 failed")

    # Test the 'top' method
    if stack.top() == 10:
        print("Test 5 passed")
    else:
        print("Test 5 failed")

    # Test the 'pop' method
    if stack.pop() == 10 and stack.size() == 10:
        print("Test 6 passed")
    else:
        print("Test 6 failed")

    # Test the 'clear' method
    stack.clear()
    if stack == Stack():
        print("Test 7 passed")
    else:
        print("Test 7 failed")

    # Test the 'is_empty' method
    if stack.is_empty() and not other_stack.is_empty():
        print("Test 8 passed")
    else:
        print("Test 9 failed")


if __name__ == "__main__":
    main()
