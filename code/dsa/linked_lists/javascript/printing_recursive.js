function printLinkedList(head) {
    if (head === null ) {
        return
    }
    console.log(head.value);
    printLinkedList(head.next);
}
