class MyLinkedList:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def get(self, index: int) -> int:
        current = self
        counter = 0
        while current is not None:
            if counter == index and current.val != None:
                return current.val
            current = current.next
            counter += 1
        return -1

    def addAtHead(self, val: int) -> None:
        if self.val is None:
            self.val = val
        else:
            old_val = self.val
            self.val = val
            old_next = self.next
            self.next = MyLinkedList(old_val)
            self.next.next = old_next

    def addAtTail(self, val: int) -> None:
        next_value = self.next
        prev = self
        while next_value is not None:
            prev = next_value
            next_value = next_value.next
        if prev.val is None:
            prev.val = val
        else:
            prev.next = MyLinkedList(val)

    def addAtIndex(self, index: int, val: int) -> None:
        current = self
        counter = 0
        prev = current
        while current is not None:
            prev = current
            if counter == index:
                old_val = current.val
                current.val = val
                old_next = current.next
                current.next = MyLinkedList(old_val)
                current.next.next = old_next
                return
            counter += 1
            current = current.next
        prev.next = MyLinkedList(val)

    def deleteAtIndex(self, index: int) -> None:
        current = self
        counter = 0
        prev = None
        print(index)
        while current is not None:
            if counter == index:
                old_next = current.next
                if old_next is not None:
                    current.val = old_next.val
                    current.next = old_next.next
                elif prev is not None:
                    prev.next = None
                else:
                    self.val = None
            counter += 1
            prev = current
            current = current.next

    def __str__(self):
        as_list = []
        current = self
        while current is not None:
            as_list.append(current.val)
            current = current.next
        return f"LinkedList: {as_list}".replace("[", "<").replace("]", ">")


def test_two():
    methods = [
        "MyLinkedList",
        "addAtHead",
        "addAtHead",
        "addAtHead",
        "addAtIndex",
        "deleteAtIndex",
        "addAtHead",
        "addAtTail",
        "get",
        "addAtHead",
        "addAtIndex",
        "addAtHead",
    ]
    vals = [[], [7], [2], [1], [3, 0], [2], [6], [4], [4], [4], [5, 0], [6]]
    test(methods, vals)


def test_one():
    m = [
        "MyLinkedList",
        "addAtHead",
        "addAtTail",
        "addAtIndex",
        "get",
        "deleteAtIndex",
        "get",
    ]
    v = [[], [1], [3], [1, 2], [1], [1], [1]]
    test(m, v)


def test_three():
    m = ["MyLinkedList", "addAtTail", "get"]
    v = [[], [1], [0]]
    test(m, v)


def test_four():
    m = [
        "MyLinkedList",
        "addAtHead",
        "addAtTail",
        "addAtIndex",
        "get",
        "deleteAtIndex",
        "get",
        "get",
        "deleteAtIndex",
        "deleteAtIndex",
        "get",
        "deleteAtIndex",
        "get",
    ]
    v = [[], [1], [3], [1, 2], [1], [1], [1], [3], [3], [0], [0], [0], [0]]
    test(m, v)


def test(methods, vals):
    print("************************NEW TEST************************")
    a = MyLinkedList()
    returns = []
    for method, val in zip(methods[1:], vals[1:]):
        print(a)
        func = getattr(a, method)
        result = func(*val)
        returns.append(result)
        print(f"a.{method}({val})=".replace("[", "").replace("]", ""), result)
        print("*" * 10)
    print(a)
    print(returns)
    print("*" * 56)


if __name__ == "__main__":
    # some tests for this
    # test_one()
    # test_two()
    # test_three()
    test_four()
