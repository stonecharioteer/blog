from .definition import Node


def create_linked_list(array):
    """Creates a linked list from a list of items"""
    head = Node(value=array[0])
    current = head
    if len(array) > 1:
        for val in array[1:]:
            next_item = Node(value=val)
            current.next = next_item
            current = next_item
    return head
