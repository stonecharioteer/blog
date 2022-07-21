function getNodeValue(head, index) {
    for (let i = 0; i <= index; i++) {
        if (head === null) return null;

        if (i === index) return head.value;
        head = head.next;
    }
    throw `Index=${index} not found`
}
