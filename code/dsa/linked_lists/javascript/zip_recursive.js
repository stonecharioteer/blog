function zipLinkedList(head1, head2) {
    if ((head1 === null) && (head2 === null)) return null;
    if ((head1 === null) && (head2 !== null)) return head2;
    if ((head1 !== null) && (head2 === null)) return head1;

    let head1_next = head1.next;
    let head2_next = head2.next;
    head1.next = head2.next;
    head2.next = zipLinkedList(head1_next, head2_next);
    return head1;
}
