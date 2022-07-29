def zip_linked_lists(head1, head2):
    """Zips two linked lists together."""
    tail = head1
    current1 = head1
    current2 = head2
    count = 0
    while (current1 is not None) and (current2 is not None):
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        tail = tail.next
        count += 1
    if current1 is not None:
        tail.next = current1
    if current2 is not None:
        tail.next = current2
    return head1
