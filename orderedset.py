"""
This module implements the Ordered Set data structure.
Dupeless List is useful to maintain the order and at the
same time avoid duplication.

Important note: as seen in the code below, this datatype
implements only part of the operations of the available
in the regular set datatype of the Python. You can extend
it as far as you wish.
"""


class OrderedSet:
    def __init__(self, elements=[]):
        self._elements = []
        for element in elements:
            if element not in self._elements:
                self._elements.append(element)

    def __getitem__(self, idx):
        return self._elements[idx]

    def __contains__(self, element):
        return element in self._elements

    def __iter__(self):
        for i in range(len(self._elements)):
            yield self._elements[i]

    def __repr__(self):
        out = "OrderedSet({"

        if self.is_empty():
            return "{}}})".format(out)

        for element in self._elements:
            if element != self._elements[-1]:
                out += "{}, ".format(element)
        out += "{}}})".format(element)

        return out

    def __len__(self):
        return len(self._elements)

    def __eq__(self, other):
        if self._elements != other._elements:
            return False
        return True

    def __hash__(self):
        hashval = 0
        for element in self._elements:
            hashval ^= hash(element)
        return hashval

    def add(self, element):
        if element not in self._elements:
            self._elements.append(element)

    def union(self, other):
        union = OrderedSet()
        for element in self._elements:
            union.add(element)
        for element in other._elements:
            union.add(element)
        return union

    def intersection(self, other):
        intersection = OrderedSet()
        for element in self._elements:
            if element in other._elements:
                intersection.add(element)
        return intersection

    def difference(self, other):
        difference = OrderedSet()
        for element in self._elements:
            if element not in other._elements:
                difference.add(element)
        return difference

    def remove(self, element):
        if element not in self._elements:
            raise KeyError("Such element does not exist in a given set.")
        self._elements.remove(element)

    def clear(self):
        self._elements = []

    def is_empty(self):
        return self._elements == []


def main():
    """Testing OrderedSet datatype"""
    # Testing Ordered Set creation
    oset = OrderedSet({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
    if oset:
        print("Test 0 passed")
    else:
        print("Test 0 failed")

    # Testing magic method '__getitem__'
    if oset[1] == 1:
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    # Testing magic method '__contains__'
    if 7 in oset:
        print("Test 2 passed")
    else:
        print("Test 2 failed")

    # Testing magic method '__iter__'
    count = 0
    for _ in oset:
        count += 1
    if count == 10:
        print("Test 3 passed")
    else:
        print("Test 3 failed")

    # Testing magic method '__repr__'
    if str(oset) == "OrderedSet({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})":
        print("Test 4 passed")
    else:
        print("Test 4 failed")

    # Testing magic method '__len__'
    if len(oset) == 10:
        print("Test 5 passed")
    else:
        print("Test 5 failed")

    # Testing magic method '__eq__'
    if oset == OrderedSet({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}):
        print("Test 6 passed")
    else:
        print("Test 6 failed")

    # Testing magic method '__hash__'
    if {oset: oset}:
        print("Test 7 passed")
    else:
        print("Test 7 failed")

    # Testing method 'add'
    oset.add(10)
    if 10 in oset:
        print("Test 8 passed")
    else:
        print("Test 8 failed")

    # Testing method 'union'
    anotheroset = OrderedSet({11, 12})
    newoset = oset.union(anotheroset)
    if newoset == OrderedSet({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}):
        print("Test 9 passed")
    else:
        print("Test 9 failed")

    # Testing method 'difference'
    newoset = oset.difference(newoset)
    if newoset == OrderedSet({}):
        print("Test 10 passed")
    else:
        print("Test 10 failed")

    # Testing method 'remove'
    oset.remove(9)
    oset.remove(8)
    if oset == OrderedSet({0, 1, 2, 3, 4, 5, 6, 7, 10}):
        print("Test 11 passed")
    else:
        print("Test 11 failed")

    # Testing method 'clear'
    oset.clear()
    if oset == OrderedSet({}):
        print("Test 12 passed")
    else:
        print("Test 12 faled")

    # Testing method 'is_empty'
    if oset.is_empty:
        print("Test 13 passed")
    else:
        print("Test 13 failed")


if __name__ == "__main__":
    main()
