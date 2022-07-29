function findLinkedList(head, value) {
    if (head.value === value){
        return true
    }
    if (head === null) {
        return false
    }
    return findLinkedList(head.next, value)
}
