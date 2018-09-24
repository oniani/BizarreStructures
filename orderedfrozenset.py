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

    def __iter__(self):
        return sorted(super().__iter__()).__iter__()

    def __contains__(self, item):
        return super().__contains__(item)


def main():
    ofset = OrderedFrozenSet([1,2,3])
    print(ofset)
    print(ofset[0])
    print(ofset[1])
    print(ofset[2])

    for element in ofset:
        print(element)

    print(ofset)
    print(hash(ofset))

    print(1 in ofset)
    print(5 in ofset)


if __name__ == "__main__":
    main()
