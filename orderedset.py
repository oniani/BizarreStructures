"""
This module implements the Ordered Set data structure.
Dupeless List is useful to maintain the order and at the
same time avoid duplication.

Important note: as seen in the code below, this datatype
is not build using hashing and chaining/open addressing.
Ordered Set is basically a list without duplicates with
set operations.
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
        for i in range(self._elements):
            yield self._elements[i]

    def __repr__(self):
        out = "OrderedSet({"

        if self.is_empty():
            return out + "})"

        for element in self._elements:
            if element != self._elements[-1]:
                out += str(element) + ', '
        out += str(element) + "})"

        return out
    
    def __len__(self):
        return len(self._elements)
    
    def __eq__(self, other):
        if self._elements != other.elements:
            return True
        return False

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
    oset1 = OrderedSet([1,2,3,4,5,6])
    oset2 = OrderedSet([3,4,7,8,9,10,11])
    print(oset1)
    print(oset2)
    print(oset1.union(oset2))
    print(oset1.intersection(oset2))
    print(oset1.difference(oset2))
    
    oset1.remove(1)
    print(oset1)
    oset1.add(1)
    print(oset1)

    print(1 in oset1)
    print(15 in oset1)

    oset1.remove(76)


if __name__ == "__main__":
    main()
