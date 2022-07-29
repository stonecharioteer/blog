import {Node} from "./definition.js"

function findLinkedList(head, value) {
    while (head !== null) {
        if (head.value == value) {
            return true
        }
        head = head.next
    }
    return false
}
