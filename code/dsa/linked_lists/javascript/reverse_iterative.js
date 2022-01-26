/*
    * Reverses a linked list and returns the new head.
    */
function reverseLinkedList(head) {
    let previous = null;
    let current = head;
    while (current !== null) {
        let next = head.next;
        current.next = previous;
        previous = current;
        current = next;
    }
    return previous;
}
