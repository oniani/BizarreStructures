"""
This module implements Frozen Dictionary datatype.
The idea is the same as in Frozen Set - once the
Frozen Dictionary is created, there is no way to
change it. Thus, this is an immutable datatype.

Note: There was a proposal (PEP 416) to implement
it on a low level in Python, but the proposal was
rejected. For more information, follow the link:
https://www.python.org/dev/peps/pep-0416/
"""


class FrozenDictionary:
    def __init__(self, *args, **kwargs):
        self._dict = dict(*args, **kwargs)

    def __getitem__(self, key):
        return self._dict[key]

    def __len__(self):
        return len(self._dict)

    def __eq__(self, other):
        return self._dict == other._dict

    def __iter__(self):
        return iter(self._dict)

    def __contains__(self, key):
        return key in self._dict

    def __repr__(self):
        return "FrozenDictionary({})".format(self._dict)

    def __hash__(self):
        hashval = 0
        for key in self:
            val = self[key]
            hashval ^= hash((key, val))
        return hashval


def main():
    """Testing FrozenDictionary datatype"""
    # Testing Frozen Dictionary creation
    fdict = FrozenDictionary({"a": 0, "b": 1, "c": 2})
    if fdict:
        print("Test 0 passed")
    else:
        print("Test 0 failed")

    # Testing magic method '__getitem__'
    if fdict["c"] == 2:
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    # Testing magic method '__len__'
    if len(fdict) == 3:
        print("Test 2 passed")
    else:
        print("Test 2 failed")

    # Testing magic method '__eq__'
    if fdict == FrozenDictionary({"a": 0, "b": 1, "c": 2}):
        print("Test 3 passed")
    else:
        print("Test 3 failed")

    # Testing magic method '__iter__'
    num = 0
    res = True
    for key in fdict:
        if fdict[key] != num:
            res = False
        num += 1
    if res:
        print("Test 4 passed")
    else:
        print("Test 4 failed")

    # Testing magic method '__contains__'
    if "c" in fdict:
        print("Test 5 passed")
    else:
        print("Test 5 failed")

    # Testing magic method '__repr__'
    if str(fdict) == "FrozenDictionary({'a': 0, 'b': 1, 'c': 2})":
        print("Test 6 passed")
    else:
        print("Test 6 failed")

    # Testing magic method '__hash__'
    if hash(fdict):
        regular_dict = {fdict: 1, 2: 3}
        if regular_dict:
            print("Test 7 passed")
    else:
        print("Test 7 failed")


if __name__ == "__main__":
    main()
