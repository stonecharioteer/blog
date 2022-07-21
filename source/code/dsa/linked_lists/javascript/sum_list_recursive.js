import {Node} from "./definition.js"


function sumLinkedList(head, sum=0) {
    if (head === null) {
        return 0
    } else {
        sum += head.value;
        sum += sumLinkedList(head.next);
        return sum
    }
}
