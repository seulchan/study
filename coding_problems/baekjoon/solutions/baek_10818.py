# https://www.acmicpc.net/problem/10818
# memory usage: 148860 KB, time usage: 404 ms
import sys


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, sys.stdin.readline().split()))

    print(min(nums), max(nums))