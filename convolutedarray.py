"""
This module implements the Convoluted Array data structure.
It is rather interesting than useful data structure.
P.S. It does have some limited uses :)
"""

class ConvolutedArray:
    def __init__(self, items):
        self._items = items
    
    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, idx):
        return self._items[idx]
    
    def __contains__(self, item):
        return item in self._items

    def __repr__(self):
        out = "ConvolutedArray(["

        if self.is_empty():
            return out + "])"

        elif len(self._items) == 1:
            return out + str(self._items[0]) + "])"
        
        elif len(self._items) == 2:
            return out + str(self._items[0]) + ", " + str(self._items[1]) + "])"

        elif len(self._items) % 2 == 0:
            for i in range(len(self._items)):
                if i < len(self._items) // 2 - 1:
                    out += str(self._items[i]) + ", ["
                elif i == len(self._items) // 2 - 1:
                    out += str(self._items[i]) + ", "
                elif i == len(self._items) // 2:
                    out += str(self._items[i]) + "], "
                elif i < len(self._items) - 1:
                    out += str(self._items[i]) + "], "
                else:
                    out += str(self._items[i]) + "])"
        else:
            for i in range(len(self._items)):
                if i < len(self._items) // 2:
                    out += str(self._items[i]) + ", ["
                elif i == len(self._items) // 2:
                    out += str(self._items[i]) + "], "
                elif i < len(self._items) - 1:
                    out += str(self._items[i]) + "], "
                else:
                    out += str(self._items[i]) + "])"
        return out

    def get_pair(self, idx):
        if len(self._items) % 2 == 0:
            return [self._items[idx], self._items[-1-idx]]
        else:
            if idx == len(self._items) // 2:
                return [idx]
            else:
                return [self._items[idx], self._items[-1-idx]]

    def flatten(self):
        return f"ConvolutedArray({self._items})"

    def clear(self):
        self._items = []

    def is_empty(self):
        return self._items == []


def main():
    print(ConvolutedArray([]))
    print(ConvolutedArray([1]))
    print(ConvolutedArray([1,2]))
    print(ConvolutedArray([1,2,3]))
    print(ConvolutedArray([1,2,3,4]))
    print(ConvolutedArray([1,2,3,4,5]))
    print(ConvolutedArray([1,2,3,4,5,6]))
    print(ConvolutedArray([1,2,3,4,5,6,7,8,9]))
    print(ConvolutedArray([1,2,3,4,5,6,7,8,9,10]))
    print(ConvolutedArray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
    print(ConvolutedArray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))

    print(ConvolutedArray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]).flatten())

    convarr = ConvolutedArray([1,2,3,4,5,6,7,8,9,10,11,14])
    print(convarr)
    print(convarr[2])
    print(convarr.get_pair(5))
    print(convarr.get_pair(7))
    print(convarr.get_pair(6))

    convarr = ConvolutedArray([1,2,3,4,5,6,7,8,9,10,11])
    print(convarr)
    print(convarr.get_pair(1))
    print(convarr.flatten())

    print(1 in convarr)
    print(123 in convarr)


if __name__ == "__main__":
    main()
