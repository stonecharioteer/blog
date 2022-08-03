"""Sum linked List Iterative method"""


def sum_linked_list(head):
    """Iteratively gets the sum of all items in a linked list"""
    sum_list = 0
    while head is not None:
        sum_list += head.value
        head = head.next
    return sum_list
