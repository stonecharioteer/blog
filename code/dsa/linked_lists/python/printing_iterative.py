def print_linked_list(head):
    """Iteratively prints all the items in a linked list, given the head
    node"""
    current = head
    while current is not None:
        print(current.value)
        current = current.next
