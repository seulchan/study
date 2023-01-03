# https://leetcode.com/problems/design-linked-list/
# memory usage: 14.9 MB, time usage: 400 ms
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# SinglyLinkedList
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index > self.size - 1:
            return -1

        count = 0
        curr = self.head

        while curr:
            if index == count:
                return curr.val

            curr = curr.next
            count += 1

    def addAtHead(self, val: int) -> None:
        if self.head == None:
            self.head = ListNode(val)
            self.tail = self.head
            self.size += 1
            return

        prev_head = self.head
        self.head = ListNode(val)
        self.head.next = prev_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.tail == None:
            self.head = ListNode(val)
            self.tail = self.head
            self.size += 1
            return

        new_tail = ListNode(val)
        self.tail.next = new_tail
        self.tail = new_tail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.size:
            self.addAtTail(val)
            return

        count = 0
        curr = self.head

        while curr:
            if index == count + 1:
                temp = curr.next
                curr.next = ListNode(val)
                curr.next.next = temp
                self.size += 1
                return

            curr = curr.next
            count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size - 1:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        count = 0
        curr = self.head
        while curr:
            if index == count + 1:
                if index == self.size - 1:
                    curr.next = None
                    self.tail = curr
                    self.size -= 1
                    return
                curr.next = curr.next.next
                self.size -= 1
                return

            curr = curr.next
            count += 1


# DoublyLinkedList
class ListDoublyNode:
    def __init__(self, x):
        self.val = x
        self.next, self.prev = None, None


class MyDoublyLinkedList:
    def __init__(self):
        self.size = 0
        # sentinel nodes as pseudo-head and pseudo-tail
        self.head, self.tail = ListDoublyNode(0), ListDoublyNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if index is invalid
        if index < 0 or index >= self.size:
            return -1

        # choose the fastest way: to move from the head
        # or to move from the tail
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev

        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        pred, succ = self.head, self.head.next

        self.size += 1
        to_add = ListDoublyNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        succ, pred = self.tail, self.tail.prev

        self.size += 1
        to_add = ListDoublyNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # If index is greater than the length,
        # the node will not be inserted.
        if index > self.size:
            return

        # [so weird] If index is negative,
        # the node will be inserted at the head of the list.
        if index < 0:
            index = 0

        # find predecessor and successor of the node to be added
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev

        # insertion itself
        self.size += 1
        to_add = ListDoublyNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # if the index is invalid, do nothing
        if index < 0 or index >= self.size:
            return

        # find predecessor and successor of the node to be deleted
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev

        # delete pred.next
        self.size -= 1
        pred.next = succ
        succ.prev = pred


if __name__ == "__main__":
    obj = MyLinkedList()
    obj.addAtHead(2)
    obj.deleteAtIndex(1)
    obj.addAtHead(2)
    obj.addAtHead(7)
    obj.addAtHead(3)
    obj.addAtHead(2)
    obj.addAtHead(5)
    obj.addAtTail(5)
    obj.get(5)
    obj.deleteAtIndex(6)
    obj.deleteAtIndex(4)
