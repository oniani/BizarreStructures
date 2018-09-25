"""
There is nothing much to say about this module.
It wraps around the frozenset and keeps it ordered.
Besides, it includes some additional custom-made
methods which may or may not be useful.
"""


class OrderedFrozenSet(frozenset):
    def __init__(self, elements=[]):
        self = frozenset(elements)

    def __getitem__(self, idx):
        return sorted(super().__iter__()).__getitem__(idx)

    def __len__(self):
        return super().__len__()

    def __iter__(self):
        return sorted(super().__iter__()).__iter__()

    def __contains__(self, item):
        return super().__contains__(item)

    def __eq__(self, other):
        return super().__eq__(other)

    def __repr__(self):
        return super().__repr__()


def main():
    """
    Testing OrderedFrozenSet datatype
    """
    # Testing Frozen Dictionary creation
    ofset = OrderedFrozenSet({1, 2, 3})
    if ofset:
        print("Test 0 passed")
    else:
        print("Test 0 failed")

    # Testing magic method '__getitem__'
    if ofset[1] == 2:
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    # Testing magic method '__len__'
    if len(ofset) == 3:
        print("Test 2 passed")
    else:
        print("Test 2 failed")

    # Testing magic method '__iter__'
    lst = [1, 2, 3]
    res = True
    for i in range(len(ofset)):
        if ofset[i] != lst[i]:
            res = False
    if res:
        print("Test 3 passed")
    else:
        print("Test 3 failed")

    # Testing magic method '__contains__'
    if (2 in ofset) is True:
        print("Test 4 passed")
    else:
        print("Test 4 failed")

    # Testing magic method '__eq__'
    if ofset == OrderedFrozenSet({1, 2, 3}):
        print("Test 5 passed")
    else:
        print("Test 5 failed")

    # Testing magic method '__repr__'
    if str(ofset) == "OrderedFrozenSet({1, 2, 3})":
        print("Test 6 passed")
    else:
        print("Test 6 failed")


if __name__ == "__main__":
    main()
