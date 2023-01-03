# https://www.acmicpc.net/problem/2839
# memory usage: 30616 KB, time usage: 36 ms

def find_min_pack(num):
    if n % 5 == 0:
        return n // 5

    for i in range(n//5, 0, -1):
        if (n - 5 * i) % 3 == 0:
            return i + (n - 5 * i) // 3

    if n % 3 == 0:
        return n // 3

    return -1


if __name__ == "__main__":
    n = int(input())
    print(find_min_pack(n))
