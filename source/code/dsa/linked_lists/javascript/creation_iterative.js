import { Node } from './definition.js';

export function createLinkedlist(array) {
    head = Node(array[0]);
    current = head
    if ( array.len() > 1 ) {
        for ( i=1; i<array.len(); i++  ) {
            item = array[i];
        }
    }
    return head
};
