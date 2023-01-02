# https://www.acmicpc.net/problem/10799
# memory usage: 31676 KB, time usage: 60 ms
import sys

if __name__ == "__main__":
    symbols = list(sys.stdin.readline().rstrip())
    stack = []

    result = 0

    for i in range(len(symbols)):
        if symbols[i] == '(':
            stack.append(symbols[i])
        else:
            if symbols[i - 1] == '(':
                stack.pop()
                result += len(stack)
            else:
                stack.pop()
                result += 1

    print(result)
