# https://www.acmicpc.net/problem/2812
# memory usage: 57288 KB, time usage: 280 ms

n, k = map(int, input().split())
numbers = list(map(int, input()))
result = []

for i in range(n):
    while result and result[-1] < numbers[i] and k > 0:
        result.pop()
        k -= 1
    result.append(numbers[i])

while k > 0:
    result.pop()
    k -= 1

print(''.join(map(str, result)))
