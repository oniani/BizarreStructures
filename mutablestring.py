"""
This module implements the Mutable String
data structure. As the name implies, Mutable String
is a string that is mutable. This datatype also
contains some custom-made methods.

Important note: this class is uses the built-in
'str' (string) class which is NOT mutable.
"""

class MutableString:
    def __init__(self, string):
        self._string = string
    
    def __len__(self):
        return len(self._string)
    
    def __getitem__(self, idx):
        return self._string[idx]
    
    def __contains__(self, item):
        return item in self._string

    def __iter__(self):
        for i in range(len(self._string)):
            yield self._string[i]

    def __eq__(self, other):
        return self._string == other._string
    
    def __repr__(self):
        return self._string

    def reverse(self):
        self._string = self._string[::-1]

    def replace(self, string, other_string):
        self._string = self._string.replace(string, other_string)

    def capitalize(self):
        self._string = self._string.capitalize()
    
    def lower(self):
        self._string = self._string.lower()

    def upper(self):
        self._string = self._string.upper()
    
    def title(self):
        self._string = self._string.title()
    
    def swapcase(self):
        self._string = self._string.swapcase()


def main():
    a = MutableString("abc")
    a.reverse()
    a.replace('a', 'b')
    print(a.title())
    print(a)


if __name__ == "__main__":
    main()
