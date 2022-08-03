/*
    * Reverses a linked list recursively and returns the head
    */
function reverseLinkedList(head, prev=null) {
    if (head === null) return prev;
    const next = head.next;
    head.next = prev;
    return reverseLinkedList(next, head);
}
