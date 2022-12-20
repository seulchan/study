# https://leetcode.com/problems/merge-two-sorted-lists/
# memory usage: 42.3 MB, time usage: 1 ms
from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# time complexity O ( m + n )
# space complexity O ( m + n )
def merge_two_lists_recursive(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1:
        return list2
    if not list2:
        return list1

    head = None

    if list1.val < list2.val:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    head.next = merge_two_lists_recursive(list1, list2)

    return head


# Time complexity: O ( m + n )
# Space complexity: O ( 1 )
def merge_two_lists_iterative(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode()
    tail = head

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    tail.next = list2 if not list1 else list1

    return head.next


def print_all(root):
    curr = root
    while curr:
        print(curr.val, " -> ", end="")
        curr = curr.next
    print()

if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    merged_list = merge_two_lists_iterative(list1, list2)
    print_all(merged_list)
