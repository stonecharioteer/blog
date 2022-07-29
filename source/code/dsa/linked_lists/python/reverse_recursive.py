def reverse_linked_list(head, prev=None):
    """Reverses a linked list recursively"""
    if head is None:
        return prev
    else:
        next = head.next
        head.next = prev
        return reverse_linked_list(next, head)
