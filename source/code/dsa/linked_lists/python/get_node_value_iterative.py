def get_node_value(head, index):
    count = 0
    while head is not None:
        if count == index:
            return head.value
        else:
            head = head.next
    raise IndexError(f"{index} doesn't have any value!")
