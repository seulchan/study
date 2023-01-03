# https://leetcode.com/problems/implement-stack-using-queues
# memory usage: 14 MB, time usage: 33 ms
from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        if len(self.q) == 0:
            return True
        return False
