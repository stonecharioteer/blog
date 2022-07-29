def print_linked_list(head):
    """Prints the values of each item of a linked list, recursively."""
    if head is None:
        return
    else:
        print(head.value)
        print_linked_list(head.next)
