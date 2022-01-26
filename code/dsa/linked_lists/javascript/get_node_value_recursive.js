function getNodeValue(head, index) {
    if (head === null) return null;
    if (index === 0) return head.value;
    return getNodeValue(head, index-1);
}
