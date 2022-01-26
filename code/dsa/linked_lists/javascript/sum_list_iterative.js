import {Node} from "./definition.js"

function sumLinkedList(head) {
    let sumList = 0
    while (head !== null) {
        sumList += head.value;
        head = head.next;
    }
    return sumList
}
