import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from definition import Node


def sum_linked_list(head, sum_list=0):
    if head is None:
        return 0
    sum_list += head.value
    sum_list += sum_linked_list(head.next)
    return sum_list
