# https://www.acmicpc.net/problem/2953
# memory usage: 30616 KB, time usage: 36 ms
import sys


if __name__ == "__main__":
    result = [sum(map(int, sys.stdin.readline().split())) for _ in range(5)]
    print(result.index(max(result)) + 1, max(result))
