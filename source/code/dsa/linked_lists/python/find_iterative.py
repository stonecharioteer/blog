def find_iterative(head, value):
    """Find a target value in the linked list"""
    while head is not None:
        if value == head.value:
            return True
        head = head.next
    return False
