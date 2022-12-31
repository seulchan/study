# https://leetcode.com/problems/min-stack/
# memory usage: 17.8 MB, time usage: 52 ms
from typing import Optional, List


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = None

    def push(self, val: int) -> None:
        if self.min_value is None:
            self.min_value = val
        else:
            self.min_value = min(self.min_value, val)
        self.stack.append(val)

    def pop(self) -> None:
        removed = self.stack.pop()
        if removed == self.min_value:
            if len(self.stack) == 0:
                self.min_value = None
                return
            self.min_value = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value


class MinStack2:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
