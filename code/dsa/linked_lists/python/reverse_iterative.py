def reverse_linked_list(head):
    """Reverse the items in a linked list and return the new head"""
    current_node = head
    previous_node = None
    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    return previous_node
