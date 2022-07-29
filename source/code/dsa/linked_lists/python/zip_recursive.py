def zip_linked_list(head1, head2):
    if head1 is None and head2 is None:
        return None
    if head1 is None and head2 is not None:
        return head2
    if head1 is not None and head2 is None:
        return head1
    next_head1 = head1.next
    next_head2 = head2.next
    head1.next = head2
    head2.next = zip_linked_list(next_head1, next_head2)
    return head1
