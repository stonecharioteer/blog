import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import random

from definition import Node


def test_create_linked_list():
    """Tests the creation of a linked list"""
    from creation_iterative import create_linked_list

    input_list = [random.randint(0, 1000) for _ in range(500)]
    head = create_linked_list(input_list)
    current = head
    for i in input_list:
        assert isinstance(current, Node), "A linked list was not created correctly"
        assert current.value == i, "The value does not match"
        current = current.next
    assert current is None, "The last item is not None"
