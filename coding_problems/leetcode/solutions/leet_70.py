# https://leetcode.com/problems/min-stack/
# memory usage: 13.8 MB, time usage: 65 ms

def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp1 = 1
    dp2 = 2

    for i in range(n - 2):
        tmp = dp2
        dp2 = dp1 + dp2
        dp1 = tmp

    return dp2


if __name__ == "__main__":
    print(climbStairs(5))
