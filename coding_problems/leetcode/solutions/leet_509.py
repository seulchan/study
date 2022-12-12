# https://leetcode.com/problems/fibonacci-number/

def fib(n: int) -> int:
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    n = 4
    print(fib(n))