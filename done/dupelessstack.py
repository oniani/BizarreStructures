"""
This module implements the Dupeless Stack data structure.
Dupeless Stack is a stack without duplicates.
The order of the items of the stack is maintained.
"""


class DupelessStack:
    """
    Dupeless Stack class
    """
    def __init__(self, items=[]):
        self._items = []
        for item in items:
            if item not in self._items:
                self._items.append(item)

    def __contains__(self, item):
        return item in self._items

    def __eq__(self, other):
        return sorted(self._items) == sorted(other._items)

    def __repr__(self):
        out = "DupelessStack(["

        if self.is_empty():
            return "{}])".format(out)

        for item in self._items:
            if item != self._items[-1]:
                out += "{}, ".format(item)
        out += "{}])".format(item)

        return out

    def __hash__(self):
        hashval = 0
        for item in self._items:
            hashval ^= hash(item)
        return hashval

    def size(self):
        """
        Return the size of the Dupeless Stack
        """
        return len(self._items)

    def top(self):
        """
        Return the top item of the Dupeless Stack
        """
        if self.is_empty():
            raise RuntimeError("Attempt to get a top of the empty stack!")
        return self._items[-1]

    def push(self, item):
        """
        Push an item to the Dupeless Stack
        """
        if item not in self._items:
            self._items.append(item)

    def pop(self):
        """
        Pop the last item from the Dupeless Stack
        """
        if self.is_empty():
            raise RuntimeError("Attempt to pop the empty stack!")
        item = self.top()
        self._items = self._items[:-1]
        return item

    def clear(self):
        """
        Clear the Dupeless Stack
        """
        self._items = []

    def is_empty(self):
        """
        Check the emptiness of the Dupeless Stack
        """
        return self._items == []


def main():
    """
    Testing DupelessStack datatype
    """
    # Testing Dupeless Stack creation
    dls = DupelessStack([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    if dls:
        print("Test 0 passed")
    else:
        print("Test 0 failed")

    # Testing magic method '__contains__'
    if (3 in dls) is True:
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    # Testing magic method '__eq__'
    new_dls = DupelessStack([1, 5, 3, 2, 4, 12, 5])
    one_more_dls = DupelessStack([5, 4, 5, 5, 1, 2, 4, 12, 3])
    if new_dls == one_more_dls:
        print("Test 2 passed")
    else:
        print("Test 2 failed")

    # Testing magic method '__repr__'
    if str(dls) == "DupelessStack([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])":
        print("Test 3 passed")
    else:
        print("Test 3 failed")

    # Testing magic method '__hash__'
    if {DupelessStack([0, 1, 2]): 0}:
        print("Test 4 passed")
    else:
        print("Test 4 failed")

    # Testing method 'size'
    if dls.size() == 10:
        print("Test 5 passed")
    else:
        print("Test 5 failed")

    # Testing method 'top'
    if dls.top() == 9:
        print("Test 6 passed")
    else:
        print("Test 6 failed")

    # Testing method 'push'
    dls.push(10)

    if dls == DupelessStack([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
        print("Test 7 passed")
    else:
        print("Test 7 failed")

    # Testing method 'pop'
    if dls.pop() == 10:
        if dls == DupelessStack([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
            print("Test 8 passed")
    else:
        print("Test 8 failed")

    # Testing method 'clear'
    dls.clear()
    if dls == DupelessStack([]):
        print("Test 9 passed")
    else:
        print("Test 9 failed")

    # Testing method 'is_empty'
    if dls.is_empty() is True:
        print("Test 10 passed")
    else:
        print("Test 10 failed")


if __name__ == "__main__":
    main()
