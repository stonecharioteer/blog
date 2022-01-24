function printLinkedList(head) {
    while (head !== null) {
        console.log(head.value);
        head = head.next;

    }
}
