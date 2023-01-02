# https://www.acmicpc.net/problem/10828
# memory usage: 30616 KB, time usage: 44 ms
import sys


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        return 0 if self.stack else 1

    def top(self):
        return self.stack[-1] if self.stack else -1


if __name__ == "__main__":
    n = int(input())
    stack = Stack()

    for _ in range(n):
        cmd = sys.stdin.readline().split()
        if cmd[0] == "push":
            stack.push(cmd[1])
        elif cmd[0] == "pop":
            print(stack.pop())
        elif cmd[0] == "size":
            print(stack.size())
        elif cmd[0] == "empty":
            print(stack.empty())
        elif cmd[0] == "top":
            print(stack.top())
