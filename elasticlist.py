"""
This is a datatype that simulates the behavior of the "infinite" list.
ElasticList data structure can be stretched and shrinked.
"""


class ElasticList(list):
    """ElasticList data structure.

    The data structure inherits most methods from the default list.

    NOTE: We define sparsity as the frequency of None values.
        If frequency >= 50% then sparse else not.
    """

    def __init__(self, items: list = []) -> None:
        self._items = items

    def __repr__(self):
        return f"ElasticList({str(self._items)[1:-1]})"

    def stretch(self, degree: int = 2) -> None:
        """Perform a uniform stretch of the list.

        NOTE: This makes the list less sparse.
        """
        stretcher = lambda x: [x] + [
            None for i in range(len(self._items) * degree)
        ]
        self._items = sum(list(map(stretcher, self._items)), [])

    def shrink(self, filter: str = "even") -> None:
        """Perform a uniform shrink of the list.

        Either leave even-indexed values or the odd-indexed values.

        NOTE: This makes the list more sparse.
        """
        if filter == "even":
            self._items = [
                self._items[i] for i in range(len(self._items)) if i % 2 == 0
            ]
        else:
            self._items = [
                self._items[i] for i in range(len(self._items)) if i % 2 == 1
            ]


def main():
    """Testing ElasticList datatype"""
    # Testing 'ElasticList' creation
    try:
        elastic_list = ElasticList([1, 2, 3])
        print("Test 0 passed")
    except:
        print("Test 0 failed")

    # Testing magic method '__repr__'
    if repr(elastic_list) == "ElasticList(1, 2, 3)":
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    # Testing method 'stretch'
    elastic_list.stretch(3)

    if elastic_list == ElasticList(
        [
            1,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            2,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            3,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ]
    ):
        print("Test 2 passed")
    else:
        print("Test 2 failed")

    # Testing method 'shrink'
    elastic_list.shrink()

    if elastic_list == ElasticList(
        [
            1,
            None,
            None,
            None,
            None,
            2,
            None,
            None,
            None,
            None,
            3,
            None,
            None,
            None,
            None,
        ]
    ):
        print("Test 3 passed")
    else:
        print("Test 3 failed")


if __name__ == "__main__":
    main()
