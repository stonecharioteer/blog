def find_linked_list(head, value):
    if head.value == value:
        return True
    if head == None:
        return True
    return find_linked_list(head.next, value)
