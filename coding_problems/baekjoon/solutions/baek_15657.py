# https://www.acmicpc.net/problem/15657
# memory usage: 30616 KB, time usage: 60 ms
import sys
import itertools

n, m = map(int, sys.stdin.readline().split())
num_list = sorted(list(map(int, sys.stdin.readline().split())))

for result in itertools.combinations_with_replacement(num_list, m):
    print(' '.join(map(str, result)))
