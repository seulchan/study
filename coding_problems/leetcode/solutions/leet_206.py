from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time Complexity = O ( n )
# Space Complexity = O ( 1 )
def reverse_list_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    prev_node = None
    curr_node = head

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node


# Time Complexity = O ( n )
# Space Complexity = O ( n )
def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    if (head is None) or (head.next is None):
        return head

    reversed_sublist = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
    return reversed_sublist


def print_all(root):
    curr = root
    while curr:
        print(curr.val, " -> ", end="")
        curr = curr.next
    print()


if __name__ == "__main__":
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    print_all(root)
    print_all(reverse_list_iterative(root))